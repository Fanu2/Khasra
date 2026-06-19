class AreaService:

    MARLAS_PER_KANAL = 20
    KANALS_PER_KILLA = 8
    SARSHAI_PER_MARLA = 9

    @staticmethod
    def kanal_marla_to_marla(
        kanal,
        marla
    ):

        return (
            float(kanal) * 20
            + float(marla)
        )

    @staticmethod
    def marla_to_kms(
        total_marla
    ):

        total_marla = float(
            total_marla
        )

        killa = int(
            total_marla // 160
        )

        remainder = (
            total_marla % 160
        )

        kanal = int(
            remainder // 20
        )

        remainder = (
            remainder % 20
        )

        marla = int(
            remainder
        )

        fractional = (
            remainder - marla
        )

        sarshai = round(
            fractional * 9
        )

        if sarshai == 9:
            sarshai = 0
            marla += 1

        if marla == 20:
            marla = 0
            kanal += 1

        if kanal == 8:
            kanal = 0
            killa += 1

        return (
            killa,
            kanal,
            marla,
            sarshai
        )

    @staticmethod
    def format_area(
        total_marla
    ):

        killa, kanal, marla, sarshai = (
            AreaService.marla_to_kms(
                total_marla
            )
        )

        return (
            f"{killa}K-"
            f"{kanal}K-"
            f"{marla}M-"
            f"{sarshai}S"
        )