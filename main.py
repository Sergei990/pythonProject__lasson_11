from flask import Flask, render_template

from utilit import all_candidates, get_candidate, get_candidates_by_name, get_candidates_by_skill

ass = Flask(__name__)


@ass.get('/')
def all_name_candidates() -> str:
    """"Выводит  Список кандидатов """
    return render_template('list_name.html', candidate=all_candidates)


@ass.get('/candidate/<int:candidate_id>')
def one_candidate(candidate_id: int) -> str:
    """"Выводит однога кандидата по id """
    return render_template('candidates_id.html', fuck=get_candidate(candidate_id))


@ass.get('/search/<candidate_name>')
def named_candidate(candidate_name: str) -> [int, str]:
    """"Выводит кандидатов по имени """
    list, name = get_candidates_by_name(candidate_name)
    return render_template('search.html', name=name, list=list)


@ass.get('/skill/<skill_name>')
def candidates_by_skill(skill_name: str) -> [int, str]:
    """"Выводит кандида по skill"""
    list_candidates_by_skill, candidate_by_skill = get_candidates_by_skill(skill_name)

    return render_template('skill.html', list_candidates=list_candidates_by_skill, skill=candidate_by_skill)


if __name__ == '__main__':
    ass.run()
