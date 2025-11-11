"""Utilidades compartilhadas para os quizzes interativos dos módulos."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence


@dataclass(frozen=True)
class MultipleChoiceQuestion:
    """Representa uma questão de múltipla escolha com cinco alternativas."""

    prompt: str
    options: tuple[str, str, str, str, str]
    correct_index: int
    difficulty: str
    explanation: str

    def __post_init__(self) -> None:  # type: ignore[override]
        if len(self.options) != 5:
            raise ValueError("Cada questão deve conter exatamente 5 alternativas.")
        if not 0 <= self.correct_index < 5:
            raise ValueError("O índice da alternativa correta deve estar entre 0 e 4.")
        if self.difficulty not in {"básico", "intermediário", "avançado", "difícil", "extremo"}:
            raise ValueError(
                "Dificuldade deve estar entre: básico, intermediário, avançado, difícil, extremo."
            )
        if not self.prompt.strip():
            raise ValueError("Enunciado da questão não pode ser vazio.")
        if not self.explanation.strip():
            raise ValueError("A explicação/gabarito não pode ser vazia.")


@dataclass(frozen=True)
class VFStatement:
    """Afirmativa para análise verdadeiro/falso com justificativa."""

    statement: str
    is_true: bool
    rationale: str

    def __post_init__(self) -> None:  # type: ignore[override]
        if not self.statement.strip():
            raise ValueError("A afirmativa não pode ser vazia.")
        if not self.rationale.strip():
            raise ValueError("A justificativa deve ser informada para garantir gabarito robusto.")


@dataclass(frozen=True)
class EssayPrompt:
    """Questão dissertativa com subitens orientadores."""

    stem: str
    subquestions: tuple[str, ...]
    guidance: str

    def __post_init__(self) -> None:  # type: ignore[override]
        if not self.stem.strip():
            raise ValueError("O enunciado da questão dissertativa não pode ser vazio.")
        if not self.subquestions:
            raise ValueError("Cada questão dissertativa deve ter pelo menos um subitem.")
        if not 2 <= len(self.subquestions) <= 5:
            raise ValueError("Cada questão deve conter de 2 a 5 subquestões.")
        if not self.guidance.strip():
            raise ValueError("É necessário fornecer orientação/gabarito para a resposta dissertativa.")


def _normalize_mcq_answer(text: str) -> int:
    text = text.strip().upper()
    mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    if text not in mapping:
        raise ValueError("Resposta inválida. Utilize A, B, C, D ou E.")
    return mapping[text]


def _normalize_vf_answer(text: str) -> bool:
    text = text.strip().upper()
    if text in {"V", "VERDADEIRO", "TRUE", "T"}:
        return True
    if text in {"F", "FALSO", "FALSE"}:
        return False
    raise ValueError("Resposta inválida. Utilize V/F.")


def run_mcq_session(
    questions: Sequence[MultipleChoiceQuestion],
    *,
    print_func: Callable[[str], None] = print,
    input_func: Callable[[str], str] = input,
) -> int:
    """Executa sessão interativa de múltipla escolha, retornando a pontuação."""

    score = 0
    for idx, question in enumerate(questions, start=1):
        print_func(f"\nQuestão {idx} — Dificuldade: {question.difficulty.title()}")
        print_func(question.prompt)
        for option_idx, option in enumerate(question.options):
            label = chr(ord("A") + option_idx)
            print_func(f"  {label}) {option}")
        while True:
            try:
                answer = _normalize_mcq_answer(input_func("Sua resposta (A-E): "))
            except ValueError as exc:
                print_func(str(exc))
                continue
            break
        if answer == question.correct_index:
            score += 1
            print_func("✅ Correto!")
        else:
            print_func("❌ Resposta incorreta.")
        correct_letter = chr(ord("A") + question.correct_index)
        print_func(f"Gabarito: {correct_letter}. {question.explanation}\n")
    print_func(f"Pontuação final (MCQ): {score}/{len(questions)}")
    return score


def run_vf_session(
    statements: Sequence[VFStatement],
    *,
    print_func: Callable[[str], None] = print,
    input_func: Callable[[str], str] = input,
) -> int:
    """Executa sessão de verdadeiro/falso retornando a pontuação."""

    score = 0
    for idx, statement in enumerate(statements, start=1):
        print_func(f"\nAfirmativa {idx}")
        print_func(statement.statement)
        while True:
            try:
                answer = _normalize_vf_answer(input_func("Sua resposta (V/F): "))
            except ValueError as exc:
                print_func(str(exc))
                continue
            break
        if answer == statement.is_true:
            score += 1
            print_func("✅ Correto!")
        else:
            print_func("❌ Resposta incorreta.")
        label = "Verdadeiro" if statement.is_true else "Falso"
        print_func(f"Gabarito: {label}. {statement.rationale}\n")
    print_func(f"Pontuação final (V/F): {score}/{len(statements)}")
    return score


__all__ = [
    "MultipleChoiceQuestion",
    "VFStatement",
    "EssayPrompt",
    "run_mcq_session",
    "run_vf_session",
]
