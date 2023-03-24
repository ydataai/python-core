from enum import Enum, auto


class PrivacyLevel(Enum):
    """Privacy level exposed to the end-user."""
    HIGH_FIDELITY = auto()
    HIGH_PRIVACY = auto()
    BALANCED_PRIVACY_FIDELITY = auto()

    def __str__(self):
        if self.value == self.HIGH_FIDELITY.value:
            return "High Fidelity"
        if self.value == self.HIGH_PRIVACY.value:
            return "High Privacy"
        if self.value == self.BALANCED_PRIVACY_FIDELITY.value:
            return "Balanced Privacy/Fidelity"
        return "N/D"
