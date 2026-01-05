class AadhaarRecord:
    def __init__(
        self,
        aadhaar_number: str,
        age: int,
        mobile_linked: bool,
        address_changed: bool
    ):
        self.aadhaar_number = aadhaar_number
        self.age = age
        self.mobile_linked = mobile_linked
        self.address_changed = address_changed

    def to_dict(self):
        return {
            "aadhaar_number": self.aadhaar_number,
            "age": self.age,
            "mobile_linked": self.mobile_linked,
            "address_changed": self.address_changed
        }
