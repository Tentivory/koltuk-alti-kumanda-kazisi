#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk altı kumanda kazısı. Çalışır. Gereksizdir. Patates içermez."""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime

KATMANLAR = [
    "yüzey tozu (son bölümden kalma)",
    "simit kırıntısı, susamı kaçmış",
    "2014 ten kuruş, hâlâ kıymetli sanıyor",
    "tek çorap, çiftini reddetmiş",
    "eski fiş, kimse sahip çıkmaz",
    "kumanda, yüzü aşağı, onuru yerinde",
    "pil kapağı, asıl sanık bu olabilir",
]

KOLTUKLAR = {
    "kanepe": 4,
    "berjer": 3,
    "kayinvalide": 6,
    "cek yat": 5,
}


def kaz(koltuk: str, derinlik: int, hedef: str, tohum: int | None) -> dict:
    rng = random.Random(tohum if tohum is not None else datetime.now().microsecond)
    taban = KOLTUKLAR.get(koltuk, 4)
    limit = max(1, min(derinlik, len(KATMANLAR)))
    bulunan = []
    for i in range(limit):
        katman = KATMANLAR[i % len(KATMANLAR)]
        sapma = rng.choice(["sağ minder", "sol minder", "dikiş aralığı", "kolçak çukuru"])
        bulunan.append({"katman": i + 1, "eser": katman, "konum": sapma})
    kumanda = any("kumanda" in x["eser"] for x in bulunan)
    pil_bitik = rng.random() < 0.62
    karar = (
        "Kumanda bulundu. Suçlu pil. Televizyon beraat etti, şartlı."
        if kumanda and pil_bitik
        else "Kumanda bulundu. Susması utançtan. Pil şahitlik yaptı."
        if kumanda
        else "Kumanda yok. Minder ifade değiştirdi. Kazı uzatılsın."
    )
    if hedef == "pil" and not any("pil" in x["eser"] for x in bulunan):
        karar = "Pil kapağı bu derinlikte çıkmadı. Sanık firarda, koltuğun içinde."
    return {
        "daire": "TentiAŞ Minder Arkeolojisi",
        "koltuk": koltuk,
        "beklenen_derinlik": taban,
        "kazilan": limit,
        "buluntular": bulunan,
        "hedef": hedef,
        "karar": karar,
        "damga": {
            "isim": "Kayyum Grok",
            "kurum": "TentiAŞ",
            "tarih": "09 Ekim 2026",
            "no": "KG-2026-KOLTUK-041",
            "ciddiyet": "hem ciddi hem değil",
        },
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Koltuk altı resmi kumanda kazısı")
    p.add_argument("--koltuk", default="kanepe", choices=sorted(KOLTUKLAR))
    p.add_argument("--derinlik", type=int, default=6)
    p.add_argument("--hedef", default="kumanda", choices=["kumanda", "pil", "corap"])
    p.add_argument("--tohum", type=int, default=None)
    args = p.parse_args()
    tutanak = kaz(args.koltuk, args.derinlik, args.hedef, args.tohum)
    print(json.dumps(tutanak, ensure_ascii=False, indent=2))
    print()
    print("MÜHÜR: Kayyum Grok | TentiAŞ | 09 Ekim 2026 | KG-2026-KOLTUK-041")
    print("Bu çıktı ciddidir. Değildir. İkisi de dosyaya işlendi.")


if __name__ == "__main__":
    main()
