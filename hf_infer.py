#!/usr/bin/env python
import argparse, time, os, sys, textwrap
from typing import List
try:
    import torch
except Exception:
    torch = None

from transformers import pipeline

DEFAULT_TEXTS_TR = [
    "Bu filmi gerçekten çok beğendim, oyunculuk harikaydı.",
    "Hizmet berbattı, bir daha gelmem.",
    "Ürün fena değil ama fiyatına göre daha iyi olabilirdi."
]

def sanitize_cell(s: str, maxlen: int = 140) -> str:
    s = s.replace("|", "\\|").replace("\n", " ")
    if len(s) > maxlen:
        s = s[:maxlen-1] + "…"
    return s

def pick_device(choice: str) -> (str, int):
    if choice == "cpu":
        return "CPU", -1
    if choice == "cuda":
        return "GPU", 0
    # auto
    if torch is not None and getattr(torch, "cuda", None) and torch.cuda.is_available():
        return "GPU", 0
    return "CPU", -1

def load_texts(path: str | None) -> List[str]:
    if not path:
        return DEFAULT_TEXTS_TR
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.readlines() if ln.strip()]
    return lines or DEFAULT_TEXTS_TR

def main():
    parser = argparse.ArgumentParser(description="Quick HF pipeline inference + timing -> Markdown table")
    parser.add_argument("--task", choices=["text-classification", "summarization"], default="text-classification",
                        help="Which pipeline to run.")
    parser.add_argument("--model", default=None, help="Optional model id from Hugging Face Hub.")
    parser.add_argument("--device", choices=["auto", "cpu", "cuda"], default="auto",
                        help="Device preference. 'auto' picks GPU if available.")
    parser.add_argument("--texts_file", default=None, help="Path to a UTF-8 .txt file with one example per line.")
    parser.add_argument("--out", default="hf_results.md", help="Output Markdown filename.")
    parser.add_argument("--max_length", type=int, default=128, help="Max length for summarization outputs.")
    parser.add_argument("--min_length", type=int, default=20, help="Min length for summarization outputs.")
    args = parser.parse_args()

    device_name, device_idx = pick_device(args.device)

    # Choose sensible defaults per task
    model_id = args.model
    if model_id is None:
        if args.task == "text-classification":
            # Turkish sentiment model; switch to another if desired with --model
            model_id = "savasy/bert-base-turkish-sentiment-cased"
        else:
            # Multilingual summarization model (works for Turkish)
            model_id = "csebuetnlp/mT5_multilingual_XLSum"

    print(f"[i] Loading pipeline: task={args.task}, model={model_id}, device={device_name}")
    if args.task == "summarization":
        nlp = pipeline(args.task, model=model_id, device=device_idx)
    else:
        nlp = pipeline(args.task, model=model_id, device=device_idx)

    texts = load_texts(args.texts_file)
    rows = []
    for text in texts:
        start = time.perf_counter()
        if args.task == "summarization":
            out = nlp(text, max_length=args.max_length, min_length=args.min_length, do_sample=False)
            # pipeline returns list[{"summary_text": "..."}]
            result_str = out[0].get("summary_text", "").strip()
        else:
            out = nlp(text, truncation=True)
            # pipeline returns list[{"label": "POSITIVE", "score": 0.99}] or similar
            pred = out[0]
            if "label" in pred:
                result_str = f"{pred['label']} ({pred.get('score', 0.0):.3f})"
            else:
                # some models (e.g., star ratings) return 'label' like 1 star..5 stars
                result_str = str(pred)
        elapsed = time.perf_counter() - start
        rows.append((text, result_str, elapsed))

    # Write Markdown table
    header = "| Girdi | Çıktı (etiket/özet) | Süre (sn) | Cihaz |\n|---|---|---:|---|\n"
    body = "\n".join(
        f"| {sanitize_cell(inp)} | {sanitize_cell(out)} | {elapsed:.3f} | {device_name} |"
        for (inp, out, elapsed) in rows
    )
    content = f"# HF Pipeline Sonuçları\n\n" \
              f"- Tarih: {time.strftime('%Y-%m-%d %H:%M:%S')}\n" \
              f"- Görev: `{args.task}`\n" \
              f"- Model: `{model_id}`\n" \
              f"- Not: Metinler `{'varsayılan (bu dosyada gömülü)' if not args.texts_file else args.texts_file}` kaynağından alındı.\n\n" \
              + header + body + "\n"

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[✓] Yazıldı -> {os.path.abspath(args.out)}")

if __name__ == "__main__":
    main()
