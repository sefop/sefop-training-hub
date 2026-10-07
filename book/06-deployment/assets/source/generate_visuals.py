"""Regenerate Section 06 diagrams, plots, and optional animations.

Install requirements.txt into an authoring virtual environment, then run this
file from any directory. --preview-dir saves raster previews at the book's
640-pixel display width. Source data is deliberately illustrative.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from io import BytesIO
import json
import os
from pathlib import Path
import xml.etree.ElementTree as ET

# Keep authoring caches beside the checkout rather than in a protected home directory.
SOURCE = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(SOURCE.parents[3] / ".cache" / "matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from PIL import Image, ImageDraw

ASSETS = SOURCE.parent
PREVIEW_WIDTH = 640
SVG_NS = "http://www.w3.org/2000/svg"
INK = "#263746"
MUTED = "#526575"
COLORS = {
    "record": ("#e8f5e9", "#2e7d32"),
    "implementation": ("#fff0df", "#bf5700"),
    "interface": ("#e8f1fc", "#1565c0"),
    "caution": ("#fff7d6", "#8c6500"),
    "failure": ("#ffebee", "#b71c1c"),
    "neutral": ("#f0f3f5", "#607080"),
}
matplotlib.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "svg.fonttype": "path",
        "svg.hashsalt": "sefop-section-06",
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.labelcolor": INK,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
    }
)


class Canvas:
    """Compose diagrams in one coordinate system shared by static and animated output."""

    def __init__(self, height: int, title: str) -> None:
        self.figure = plt.figure(figsize=(8, height / 100), dpi=100)
        self.axes = self.figure.add_axes((0, 0, 1, 1))
        self.axes.set_xlim(0, 800)
        self.axes.set_ylim(height, 0)
        self.axes.axis("off")
        self.text(400, 30, title, size=17, weight="bold")

    def text(
        self,
        x: float,
        y: float,
        value: str,
        *,
        size: float = 12,
        color: str = INK,
        weight: str = "normal",
        align: str = "center",
    ) -> None:
        self.axes.text(
            x,
            y,
            value,
            fontsize=size,
            color=color,
            weight=weight,
            ha=align,
            va="center",
            linespacing=1.45,
        )

    def box(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        title: str,
        detail: str = "",
        kind: str = "implementation",
        *,
        dashed: bool = False,
        highlight: bool = False,
    ) -> None:
        fill, border = COLORS[kind]
        self.axes.add_patch(
            FancyBboxPatch(
                (x, y),
                width,
                height,
                boxstyle="round,pad=0,rounding_size=10",
                facecolor=fill,
                edgecolor=border,
                linewidth=3 if highlight else 1.5,
                linestyle="--" if dashed else "-",
            )
        )
        if not title:
            return
        if detail:
            self.text(x + width / 2, y + height * 0.30, title, size=12.5, weight="bold")
            self.text(x + width / 2, y + height * 0.68, detail, size=11.5, color=MUTED)
        else:
            self.text(x + width / 2, y + height / 2, title, size=12.5, weight="bold")

    def arrow(
        self,
        points: Sequence[tuple[float, float]],
        *,
        color: str = MUTED,
        dashed: bool = False,
        highlight: bool = False,
    ) -> None:
        for start, end in zip(points[:-2], points[1:-1]):
            self.axes.plot(
                [start[0], end[0]],
                [start[1], end[1]],
                color=color,
                linewidth=3 if highlight else 1.7,
                linestyle="--" if dashed else "-",
                solid_capstyle="round",
            )
        self.axes.add_patch(
            FancyArrowPatch(
                points[-2],
                points[-1],
                arrowstyle="-|>",
                mutation_scale=13,
                linewidth=3 if highlight else 1.7,
                color=color,
                linestyle="--" if dashed else "-",
                shrinkA=0,
                shrinkB=3,
            )
        )


def release_path() -> Figure:
    canvas = Canvas(350, "Follow the checked version into production")
    nodes = [
        ("Source", "commit A", "record"),
        ("Checks", "build + test A", "interface"),
        ("Retain", "artifact A", "implementation"),
        ("Deploy", "artifact A", "implementation"),
        ("Verify", "known instance", "interface"),
    ]
    for index, (title, detail, kind) in enumerate(nodes):
        x = 20 + 156 * index
        canvas.box(x, 110, 136, 92, title, detail, kind)
        if index < len(nodes) - 1:
            canvas.arrow([(x + 136, 156), (x + 156, 156)])
    canvas.text(320, 92, "pass", size=11, color=COLORS["record"][1])
    canvas.arrow([(244, 202), (244, 254)], color=COLORS["failure"][1])
    canvas.text(272, 230, "fail", size=11, color=COLORS["failure"][1], align="left")
    canvas.box(166, 259, 156, 62, "Fix the change", "No deployment", "failure")
    canvas.text(
        562, 276, "Retain the artifact that passed.\nDeploy it and verify its decision.", size=12
    )
    return canvas.figure


def docker_lifecycle(phase: int | None = None) -> Figure:
    canvas = Canvas(445, "One image can start multiple containers")
    visible = 6 if phase is None else phase
    canvas.box(
        25,
        105,
        190,
        85,
        "Build inputs v1",
        "Dockerfile + source\n+ dependencies",
        "record",
        highlight=phase == 0,
    )
    if visible >= 1:
        canvas.arrow([(215, 148), (330, 148)], highlight=phase == 1)
        canvas.text(272, 121, "build", size=12)
        canvas.box(330, 105, 165, 85, "Image v1", "Packaged files", highlight=phase == 1)
    if visible >= 2:
        canvas.arrow([(495, 148), (535, 148), (535, 112), (575, 112)], highlight=phase == 2)
        canvas.box(575, 70, 200, 84, "Container 1", "Running from v1", highlight=phase == 2)
    if visible >= 3:
        canvas.arrow([(495, 148), (535, 148), (535, 228), (575, 228)], highlight=phase == 3)
        canvas.box(575, 187, 200, 84, "Container 2", "Running from v1", highlight=phase == 3)
        canvas.text(535, 168, "run", size=11)
    if visible >= 4:
        canvas.arrow([(120, 190), (120, 310)], dashed=True, highlight=phase == 4)
        canvas.text(151, 251, "edit", size=12, align="left")
        canvas.box(
            25, 315, 190, 70, "Build inputs v2", "Changed source", "record", highlight=phase == 4
        )
    if visible >= 5:
        canvas.arrow([(215, 350), (330, 350)], highlight=phase == 5)
        canvas.text(272, 326, "rebuild", size=12)
        canvas.box(330, 315, 165, 70, "Image v2", "New package", highlight=phase == 5)
    if visible >= 6:
        canvas.arrow([(495, 350), (575, 350)], highlight=phase == 6)
        canvas.text(535, 326, "run", size=11)
        canvas.box(575, 315, 200, 70, "Next container", "Running from v2", highlight=phase == 6)
    captions = [
        "Start with the Dockerfile, application source, and dependencies.",
        "Build an image containing the version 1 files.",
        "Run a container from that image.",
        "Run another container from the same image.",
        "Editing source leaves the existing image and containers at v1.",
        "Rebuild to package the changed source as image v2.",
        "A new container can now run the changed version.",
    ]
    caption = "Existing images and containers do not change when source files are edited."
    canvas.text(400, 421, caption if phase is None else captions[phase], size=11.5, color=MUTED)
    return canvas.figure


def durable_records() -> Figure:
    canvas = Canvas(425, "Keep durable records outside the container")
    canvas.box(25, 105, 230, 215, "", kind="implementation")
    canvas.text(140, 134, "Retained image", size=13, weight="bold")
    canvas.text(140, 212, "Application\nRuntime + solver\nPackaged files", size=12)
    canvas.text(140, 288, "Used again to start", size=11, color=MUTED)
    canvas.box(330, 105, 220, 215, "", kind="neutral")
    canvas.text(440, 134, "Container", size=13, weight="bold")
    canvas.box(350, 192, 180, 103, "Writable layer", "Temporary files", "caution")
    canvas.arrow([(255, 156), (330, 156)])
    canvas.text(292, 134, "start", size=11)
    canvas.box(620, 105, 155, 215, "", kind="record")
    canvas.text(697, 140, "Durable\nrecords", size=12, weight="bold")
    canvas.text(697, 223, "Inputs\nAccepted plans\nRun history", size=11.5)
    canvas.arrow([(550, 230), (620, 230)], color=COLORS["record"][1])
    canvas.text(585, 204, "write", size=11)
    canvas.box(
        80, 351, 640, 48, "Replacing a container can discard its local files.", kind="caution"
    )
    return canvas.figure


def delivery_deadline(data: dict) -> Figure:
    canvas = Canvas(355, "Reserve time for the entire decision handoff")
    durations = list(data["delivery_budget_seconds"].values())
    assert durations == [30, 180, 60, 30] and sum(durations) == 300
    phases = [
        ("Prepare", "30 seconds", "interface"),
        ("Primary solve", "180 seconds", "implementation"),
        ("Alternative", "60 seconds", "caution"),
        ("Check + deliver", "30 seconds", "record"),
    ]
    left, width, elapsed = 40, 720, 0
    centers: list[float] = []
    for seconds, (_, _, kind) in zip(durations, phases):
        x, section_width = left + width * elapsed / 300, width * seconds / 300
        fill, border = COLORS[kind]
        canvas.axes.add_patch(
            Rectangle((x, 142), section_width, 58, facecolor=fill, edgecolor=border, linewidth=1.5)
        )
        centers.append(x + section_width / 2)
        elapsed += seconds
    # Short phases are labeled outside the proportional bar, not widened to fit.
    for index, ((label, duration, _), center) in enumerate(zip(phases, centers)):
        below = index in (0, 3)
        label_x = 755 if index == 3 else center
        alignment = "right" if index == 3 else "center"
        canvas.text(label_x, 246 if below else 99, label, size=11.5, weight="bold", align=alignment)
        canvas.text(label_x, 270 if below else 121, duration, size=11, color=MUTED, align=alignment)
        canvas.axes.plot(
            [center, center], [200, 225] if below else [129, 142], color=MUTED, linewidth=1
        )
    for seconds in (0, 30, 210, 270, 300):
        x = left + width * seconds / 300
        canvas.text(x, 217, f"{seconds // 60}:{seconds % 60:02}", size=10, color=MUTED)
    canvas.axes.plot([760, 760], [68, 290], color=COLORS["failure"][1], linewidth=2, linestyle="--")
    canvas.text(752, 70, "Business deadline", align="right", size=11, color=COLORS["failure"][1])
    canvas.text(
        400,
        325,
        "Illustrative five-minute budget; segment widths represent elapsed time.",
        size=11,
        color=MUTED,
    )
    return canvas.figure


def shadow_flow(phase: int | None = None) -> Figure:
    canvas = Canvas(415, "Compare both versions; use only the current proposal")
    visible = 3 if phase is None else phase
    canvas.box(
        25, 160, 190, 94, "Input snapshot", "Same instance + data", "record", highlight=phase == 0
    )
    if visible >= 1:
        canvas.arrow([(215, 207), (245, 207), (245, 117), (280, 117)], highlight=phase == 1)
        canvas.arrow(
            [(215, 207), (245, 207), (245, 286), (280, 286)], dashed=True, highlight=phase == 1
        )
        canvas.box(280, 75, 185, 84, "Current version", "Current proposal", highlight=phase == 1)
        canvas.box(
            280, 244, 185, 84, "Candidate", "Shadow proposal", dashed=True, highlight=phase == 1
        )
    if visible >= 3:
        canvas.arrow(
            [(465, 142), (505, 142), (505, 230), (555, 230)],
            color=COLORS["interface"][1],
            highlight=phase == 3,
        )
        canvas.arrow(
            [(465, 286), (555, 286)],
            color=COLORS["interface"][1],
            dashed=True,
            highlight=phase == 3,
        )
        canvas.box(
            555, 206, 220, 99, "Compare", "Common measures", "interface", highlight=phase == 3
        )
    if visible >= 2:
        canvas.arrow([(465, 104), (555, 104)], color=COLORS["record"][1], highlight=phase == 2)
        canvas.box(
            555,
            65,
            220,
            80,
            "Operational decision",
            "Current proposal only",
            "record",
            highlight=phase == 2,
        )
    captions = [
        "Capture one input snapshot for both versions.",
        "Give identical inputs to the current and candidate versions.",
        "Deliver the current proposal without waiting for the shadow comparison.",
        "Compare proposals; the candidate still does not feed operations.",
    ]
    canvas.text(
        400,
        378,
        (
            "A shadow proposal estimates an effect; it has no observed execution outcome."
            if phase is None
            else captions[phase]
        ),
        size=11.5,
        color=MUTED,
    )
    return canvas.figure


def decision_lineage() -> Figure:
    canvas = Canvas(385, "Follow one departure through four distinct records")
    nodes = [
        ("Proposed load", "Predicted revenue"),
        ("Accepted load", "Planner's choice"),
        ("Executed load", "Pallets flown"),
        ("Observed\noutcome", "Actual revenue"),
    ]
    for index, (title, detail) in enumerate(nodes):
        x = 22 + index * 198
        canvas.box(x, 188, 162, 94, title, detail, "record")
        if index < 3:
            canvas.arrow([(x + 162, 235), (x + 198, 235)])
    canvas.box(222, 65, 158, 64, "Planner\nchanges", kind="interface")
    canvas.arrow([(301, 129), (301, 188)], color=COLORS["interface"][1])
    canvas.box(412, 65, 170, 64, "Operational\nevents", kind="caution")
    canvas.arrow([(497, 129), (497, 188)], color=COLORS["caution"][1])
    canvas.text(
        400,
        336,
        "Link every record to the departure and relevant input snapshot.",
        size=12,
        color=MUTED,
    )
    return canvas.figure


def paired_differences(data: dict) -> Figure:
    series = data["paired_release"]
    instances = series["instances"]
    values = [item["difference_percent"] for item in instances]
    assert values == [2, 2, 2, -3] and sum(values) / len(values) == 0.75
    figure, axes = plt.subplots(figsize=(8, 5.5), dpi=100)
    figure.subplots_adjust(left=0.29, right=0.95, top=0.76, bottom=0.36)
    figure.text(
        0.5,
        0.95,
        "A positive average can hide a critical regression",
        ha="center",
        fontsize=16,
        weight="bold",
    )
    figure.text(
        0.5,
        0.89,
        "Illustrative paired results: identical input snapshots for both versions",
        ha="center",
        fontsize=11,
        color=MUTED,
    )
    axes.set_xlim(-4, 3)
    axes.set_ylim(3.65, -0.65)
    axes.axvspan(-4, series["noncritical_tolerance_percent"], color="#ffebee", zorder=0)
    axes.axvline(0, color=INK, linewidth=1.5)
    axes.axvline(
        series["noncritical_tolerance_percent"],
        color=COLORS["caution"][1],
        linestyle="--",
        linewidth=1.5,
    )
    for index, item in enumerate(instances):
        critical = item["critical"]
        value = item["difference_percent"]
        axes.plot([0, value], [index, index], color=MUTED, linewidth=1.6)
        axes.scatter(
            value,
            index,
            s=150 if critical else 100,
            marker="D" if critical else "o",
            color=COLORS["failure" if critical else "record"][1],
            zorder=3,
        )
        axes.annotate(
            f"{value:+g}%",
            (value, index),
            xytext=(0, -18),
            textcoords="offset points",
            ha="center",
            fontsize=12,
            weight="bold",
        )
    axes.set_yticks(range(len(instances)), [item["label"] for item in instances])
    axes.set_xticks(range(-4, 4))
    axes.set_xlabel("Candidate minus current revenue (%)", labelpad=11)
    axes.grid(axis="x", color="#dfe5e9", linewidth=0.7)
    axes.set_axisbelow(True)
    axes.tick_params(axis="y", length=0, pad=10)
    for side in ("top", "right", "left"):
        axes.spines[side].set_visible(False)
    figure.text(
        0.30,
        0.19,
        "Dashed line: −1% tolerance for noncritical instances.",
        fontsize=11,
        color=MUTED,
    )
    figure.text(
        0.30,
        0.135,
        "Critical instance: no loss allowed (0%); investigate −3%.",
        fontsize=11,
        color=COLORS["failure"][1],
    )
    figure.text(
        0.30,
        0.07,
        "Mean difference: +0.75%    •    One critical instance fails.",
        fontsize=12,
        weight="bold",
    )
    return figure


def instance_growth(data: dict) -> Figure:
    series = data["instance_growth"]
    runs = series["runs"]
    figure, axes = plt.subplots(figsize=(8, 4.8), dpi=100)
    figure.subplots_adjust(left=0.12, right=0.96, top=0.78, bottom=0.24)
    figure.text(
        0.5,
        0.95,
        "Watch solve duration approach the available budget",
        ha="center",
        fontsize=16,
        weight="bold",
    )
    figure.text(
        0.5,
        0.885,
        "Illustrative runs • same release and hardware • comparable cargo instances",
        ha="center",
        fontsize=11,
        color=MUTED,
    )
    axes.axhspan(150, 180, color="#fff7d6", zorder=0)
    axes.axhline(
        series["primary_solve_budget_seconds"],
        color=COLORS["failure"][1],
        linewidth=1.7,
        linestyle="--",
    )
    axes.text(10, 185, "Primary solve budget: 180 seconds", fontsize=11, color=COLORS["failure"][1])
    axes.scatter(
        [run["products"] for run in runs],
        [run["solve_seconds"] for run in runs],
        s=85,
        color=COLORS["implementation"][1],
        edgecolor="white",
        linewidth=0.8,
        zorder=3,
    )
    axes.annotate(
        "Little time left\nwithin this budget",
        xy=(55, 176),
        xytext=(27, 135),
        fontsize=11,
        arrowprops={"arrowstyle": "->", "color": MUTED},
        color=INK,
    )
    axes.set(
        xlim=(7, 58),
        ylim=(0, 205),
        xlabel="Products in the instance",
        ylabel="Solve duration (seconds)",
    )
    axes.grid(color="#dfe5e9", linewidth=0.7)
    axes.set_axisbelow(True)
    for side in ("top", "right"):
        axes.spines[side].set_visible(False)
    figure.text(
        0.12,
        0.10,
        "Each point is one run. No fitted scaling law is implied.",
        fontsize=11,
        color=MUTED,
    )
    return figure


def annotate_svg(path: Path, title: str, description: str) -> None:
    """Give exported vectors accessible names without changing their geometry."""
    # Insert into the existing SVG text to preserve Matplotlib's namespaces.
    text = path.read_text(encoding="utf-8")
    start = text.index(">", text.index("<svg")) + 1
    import html

    accessible = f"\n <title>{html.escape(title)}</title>\n <desc>{html.escape(description)}</desc>"
    path.write_text(text[:start] + accessible + text[start:], encoding="utf-8")
    assert ET.parse(path).getroot().tag == f"{{{SVG_NS}}}svg"


def save_static(
    figure: Figure,
    name: str,
    title: str,
    description: str,
    preview_dir: Path | None,
) -> None:
    """Save a vector figure and, when requested, its matching displayed-size preview."""
    figure.savefig(
        ASSETS / f"{name}.svg",
        metadata={"Date": None, "Creator": "SEFOP Section 06 figure generator"},
    )
    annotate_svg(ASSETS / f"{name}.svg", title, description)
    if preview_dir is not None:
        figure.savefig(preview_dir / f"{name}.png", dpi=PREVIEW_WIDTH / figure.get_figwidth())
    plt.close(figure)


def save_animation(
    scene: Callable[[int], Figure], phases: int, name: str, preview_dir: Path | None
) -> None:
    """Animate the same scene geometry used by its complete static explanation."""
    frames: list[Image.Image] = []
    for phase in range(phases):
        figure = scene(phase)
        buffer = BytesIO()
        figure.savefig(buffer, format="png", dpi=100)
        plt.close(figure)
        buffer.seek(0)
        frames.append(Image.open(buffer).convert("RGB"))
    frames[0].save(
        ASSETS / f"{name}.gif",
        save_all=True,
        append_images=frames[1:],
        duration=1800,
        loop=0,
        disposal=2,
        optimize=False,
    )
    if preview_dir is not None:
        thumb_height = round(frames[0].height * 320 / frames[0].width)
        contact_sheet = Image.new("RGB", (640, (thumb_height + 26) * ((phases + 1) // 2)), "white")
        draw = ImageDraw.Draw(contact_sheet)
        for phase, frame in enumerate(frames):
            x, y = (phase % 2) * 320, (phase // 2) * (thumb_height + 26)
            contact_sheet.paste(
                frame.resize((320, thumb_height), Image.Resampling.LANCZOS), (x, y + 26)
            )
            draw.text((x + 10, y + 7), f"Step {phase + 1}", fill=INK)
        contact_sheet.save(preview_dir / f"{name}-frames.png")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-dir", type=Path)
    args = parser.parse_args()
    if args.preview_dir is not None:
        args.preview_dir.mkdir(parents=True, exist_ok=True)
    data = json.loads((SOURCE / "visual-data.json").read_text(encoding="utf-8"))
    specifications = [
        (
            release_path(),
            "release-path-checked-release",
            "Checked release path",
            "Source commit A passes checks, produces retained artifact A, is deployed and verified; failed checks stop deployment.",
        ),
        (
            docker_lifecycle(),
            "packaging-image-lifecycle",
            "Docker image and container lifecycle",
            "One image starts two containers. Editing source leaves them unchanged; rebuilding produces a new image for the next container.",
        ),
        (
            durable_records(),
            "packaging-durable-records",
            "Durable records outside a container",
            "A retained image starts a container with temporary writable files. Inputs, accepted plans, and run history are stored externally.",
        ),
        (
            delivery_deadline(data),
            "run-failures-delivery-deadline",
            "Five-minute delivery budget",
            "A proportional 300-second budget allocates 30 seconds preparation, 180 primary solve, 60 alternative, and 30 checking and delivery.",
        ),
        (
            paired_differences(data),
            "safe-release-paired-differences",
            "Illustrative paired release differences",
            "Paired changes are plus 2, plus 2, plus 2, and minus 3 percent. A plus 0.75 percent mean hides a critical departure's unacceptable loss.",
        ),
        (
            shadow_flow(),
            "safe-release-shadow-flow",
            "Shadow-run data flow",
            "One input snapshot feeds current and candidate versions. Both proposals are compared; only the current proposal feeds operations.",
        ),
        (
            instance_growth(data),
            "run-health-instance-growth",
            "Illustrative instance size and solve duration",
            "Ten comparable instances on fixed release and hardware approach the 180-second primary solve budget; the largest takes 176 seconds.",
        ),
        (
            decision_lineage(),
            "decision-quality-decision-lineage",
            "Decision records from proposal to outcome",
            "A departure links proposed, accepted, and executed loads to observed revenue. Planner changes and operational events enter at separate stages.",
        ),
    ]
    for figure, name, title, description in specifications:
        save_static(figure, name, title, description, args.preview_dir)
    save_animation(docker_lifecycle, 7, "packaging-image-lifecycle", args.preview_dir)
    save_animation(shadow_flow, 4, "safe-release-shadow-flow", args.preview_dir)
    print("Generated eight SVG figures and two GIF animations.")


if __name__ == "__main__":
    main()
