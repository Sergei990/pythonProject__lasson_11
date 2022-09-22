import json


def load_candidates_from_json(path: str) -> list[dict]:
    """"Возвращает список кандидатов"""
    with open(path, encoding='UTF-8') as file:
        return json.loads(file.read())


all_candidates = load_candidates_from_json('file.json')


def get_candidate(candidate_id: int) -> list[dict]:
    """"Возвращает одного кандидата по id"""
    for one_candidate_by_id in all_candidates:
        if one_candidate_by_id['id'] == candidate_id:
            return one_candidate_by_id


def get_candidates_by_name(candidate_name: str) -> [int, list]:
    """"Возвращает одного кандидата по имени"""
    result_candidate_name = []

    for candidates_name in all_candidates:
        if candidate_name.lower() in candidates_name['name'].lower():
            result_candidate_name.append(candidates_name['name'])

    return len(result_candidate_name), result_candidate_name


def get_candidates_by_skill(skill_name: str) -> [int, list]:
    """Возвращает кандидата по skill"""
    result_skills = []
    for candidates_by_skill in all_candidates:
        if skill_name.lower() in candidates_by_skill['skills'].lower().rsplit(','):
            result_skills.append(candidates_by_skill['name'])
    return len(result_skills), result_skills
