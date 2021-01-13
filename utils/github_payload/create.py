def create_handler(data):
    repos = data['repository']['full_name']
    url = data['repository']['html_url']
    sender = data['sender']['login']
    ref = data['ref']
    ref_type = data['ref_type']

    return "New {} \"{}\" is created by {} at {} ({})".format(ref_type, ref, sender, repos, url)

