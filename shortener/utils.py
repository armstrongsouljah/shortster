import random, string

from django.utils import timezone

chars = string.ascii_letters+string.digits

def shortcode_gen(size):
    """
    Helper function to generate unique shortcodes
    - size: int -> length of the shortcode
    """
    return "".join(
        random.choice(chars) for _ in range(size))


def update_site_visits(obj):
    obj.last_visited = timezone.now()
    obj.visit_count +=1
    obj.save(update_fields=['visit_count', 'last_visited'])
    print(obj.visit_count, obj.last_visited)
    print('updated object details')
