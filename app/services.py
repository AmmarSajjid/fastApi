class SentimentService:

    def predict(self, text: str) -> dict:
        lowered = text.lower()

        positive_words = ['good', 'great', 'excellent', 'amazing', 'happy']
        negative_words = ['bad', 'terrible', 'awful', 'sad', 'horrible']

        positive_count = sum(word in lowered for word in positive_words)
        negative_count = sum(word in lowered for word in negative_words)

        if positive_count > negative_count:
            label = "positive"
            score = 0.8
        elif negative_count > positive_count:
            label = "negative"
            score = 0.8
        else:
            label = "neutral"
            score = 0.5

        return {
            "label": label,
            "score": score,
            "input_length": len(text)
        }