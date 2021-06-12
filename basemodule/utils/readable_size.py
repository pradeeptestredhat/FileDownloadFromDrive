
class ReadableSize():

    @staticmethod
    def human_readable_size(num, suffix='B'):
        for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
            if abs(num) < 1024.0:
                return '{:.1f} {}{}'.format(num, unit, suffix)
            num /= 1024.0