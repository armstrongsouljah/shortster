import random, string

chars = string.ascii_letters+string.digits

def shortcode_gen(size):
    """
    Helper function to generate unique shortcodes
    - size: int -> length of the shortcode
    """
    return "".join(
        random.choice(chars) for _ in range(size))
