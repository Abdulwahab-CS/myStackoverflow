
from .models import Tag

"""
    helper functions
"""


def get_question_tags_as_string_list(tag_objects_list):
    tags = []
    for item in tag_objects_list:
        tags.append(dict(item)['name'])
    return tags


def lower_case_all_tags(tags):
    return [name.lower() for name in tags]


def remove_duplicate_tags(tags):
    return list(set(tags))


def are_tags_updated(old_tags, new_tags):
    if len(old_tags) != len(new_tags):
        return True
        
    set1 = set(old_tags)
    set2 = set(new_tags)
    return len(set1.difference(set2)) > 0

def update_question_tags_list(question, tags_list):
    used_tags = []
    for tag_name in tags_list:
        if Tag.objects.filter(name=tag_name).exists():
            tag = Tag.objects.get(name=tag_name)
        else:
            tag = Tag.objects.create(name=tag_name)
            
        used_tags.append(tag)

    # add tags to the question
    for tag in used_tags:
        question.tags.add(tag)

    question.save()
    return question