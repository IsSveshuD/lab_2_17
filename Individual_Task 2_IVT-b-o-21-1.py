#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


@click.group()
def cl():
    pass


"""
Добавить команды
"""


@cl.command()
@click.argument("contacts")
@click.option("-f", "--family")
@click.option("-N", "--name")
@click.option("-n", "--number")
@click.option("b", "--born")
def add_contact(contacts, family, name, number, born):
    """
    Добавить данные о человеке
    """
    contacts.append(
        {
            "family": family,
            "name": name,
            "number": number,
            "born": born
        }
    )
    with open(contacts, "w", encoding="utf-8") as file_out:
        json.dump(contacts, file_out, ensure_ascii=False, indent=4)
    click.secho("Контакт добавлен", fg='orange')


@cl.command()
@click.argument('contacts')
def display_contact(contacts):
    """
    Отобразить спискок контактов
    """
    if contacts:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 30,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^30} | {:^20} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Номер телефона",
                "Дата Рождения"
            )
        )
        print(line)

        for idx, contact in enumerate(contacts, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<30} | {:>20} |'.format(
                    idx,
                    contact.get('family', ''),
                    contact.get('name', ''),
                    contact.get('number', 0),
                    '.'.join((str(i) for i in contact['born']))
                )
            )
        print(line)
    else:
        print("Список контктов пуст.")


@cl.command()
@click.argument('contacts')
@click.option("-s", "--select")
def select_contact(contacts, period):
    """
    Выбрать контакт
    """
    result = []
    for contact in contacts:
        if contact.get('family') == period:
            result.append(contact)

    return result


def load_contacts(file_name):
    """
    Загрузить все контакты.
    """
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    cl()


if __name__ == "__main__":
    main()
