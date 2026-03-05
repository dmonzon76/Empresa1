# apps/customers/utils.py

def generate_client_number(customer):
    """
   Generates a client_number based on the client's category.
   If there is no category, uses a generic prefix.
    """

    category = customer.category

    if category:
        # Increase the category sequence and generate a number like "VIP-00001", "CORP-00002", etc.
        seq = category.next_sequence()
        prefix = category.prefix or ""
        return f"{prefix}{seq:05d}"

    # If it has no assigned category, use a generic prefix with the customer ID (or a temporary value if not saved yet).
    
    return f"CUST-{customer.id or 'TEMP'}"

def generate_customer_number(customer):
    """
    Generates a unique number based on the customer category.
    """
    category = customer.category

    if category:
        seq = category.next_sequence()
        prefix = category.prefix or ""
        return f"{prefix}{seq:05d}"

    # fallback if it has no category
    return f"CUST-{customer.id or 'TEMP'}"