class Predictor:
    def predict(self, text: str) -> dict:
        length = len(text)
        return {
            "length": length,
            "prediction": "positive" if length % 2 == 0 else "negative"
        }
