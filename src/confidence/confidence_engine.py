class ConfidenceEngine:

    @staticmethod
    def merge(conf1, conf2):

        merged = {}

        keys = set(conf1.keys()) | set(conf2.keys())

        for key in keys:

            merged[key] = max(

                conf1.get(key, 0),

                conf2.get(key, 0)

            )

        return merged