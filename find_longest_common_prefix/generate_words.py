#!/usr/bin/env python3
"""Generate random words sharing a prefix and save them as a one-column CSV."""

import argparse
import csv
import random
import string
from pathlib import Path


DEFAULT_COUNT = 10_000_000
DEFAULT_MIN_LENGTH = 5
DEFAULT_MAX_LENGTH = 20
DEFAULT_OUTPUT = Path(__file__).parent / "data" / "words_for_prefix_search.csv"
ALPHABET = string.ascii_lowercase


def generate_words(
    prefix: str,
    count: int,
    min_length: int,
    max_length: int,
    output: Path,
    seed: int | None = None,
) -> None:
    """Generate ``count`` random words beginning with ``prefix``."""
    if not prefix:
        raise ValueError("El prefijo no puede estar vacío.")
    if count < 1:
        raise ValueError("La cantidad de palabras debe ser positiva.")
    if min_length < 1 or max_length < min_length:
        raise ValueError("El rango de longitudes no es válido.")
    if len(prefix) > max_length:
        raise ValueError("El prefijo no puede ser más largo que la longitud máxima.")

    generator = random.Random(seed)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        for _ in range(count):
            length = generator.randint(max(min_length, len(prefix)), max_length)

            suffix = "".join(generator.choices(ALPHABET, k=length - len(prefix)))

            writer.writerow((prefix + suffix,))


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera palabras aleatorias con un prefijo común."
    )
    parser.add_argument("prefix", help="Prefijo común de las palabras.")
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=DEFAULT_COUNT,
        help=f"Número de palabras (por defecto: {DEFAULT_COUNT}).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"CSV de salida (por defecto: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "--min-length",
        type=int,
        default=DEFAULT_MIN_LENGTH,
        help=f"Longitud mínima (por defecto: {DEFAULT_MIN_LENGTH}).",
    )
    parser.add_argument(
        "--max-length",
        type=int,
        default=DEFAULT_MAX_LENGTH,
        help=f"Longitud máxima (por defecto: {DEFAULT_MAX_LENGTH}).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Semilla opcional para poder repetir la misma generación.",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    try:
        generate_words(
            prefix=arguments.prefix,
            count=arguments.count,
            min_length=arguments.min_length,
            max_length=arguments.max_length,
            output=arguments.output,
            seed=arguments.seed,
        )
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

    print(f"Se han generado {arguments.count:,} palabras en {arguments.output}")


if __name__ == "__main__":
    main()
