from experience.models import Experience


def get_timeline_experiences(timeline):
    experiences = []
    for exp_id in timeline:
        try:
            exp = Experience.objects.get(id=exp_id)
            experiences.append(exp)
        except Experience.DoesNotExist:
            raise ValueError("Experience with id {} does not exist".format(exp_id))

    return experiences
