from SRP import Mail


class Order:
    def __init__(self):
        pass

    def place_order(self):
        try:
            # Place order code goes here
            Mail.send_mail()
        except Exception as ex:
            raise  # Prefer 'raise' to preserve original traceback