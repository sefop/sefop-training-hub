# Section 06 figure sources

These files are authoring tools, separate from the language-agnostic chapter material.

Install `requirements.txt` in an authoring virtual environment, then run `generate_visuals.py`.
The script writes eight static SVG figures and two optional GIF animations into the parent asset
directory. Its paths are relative to the script, so it can be run from any working directory.

From the repository root, with Python 3.11 or later in an authoring virtual environment:

```text
python -m pip install -r book/06-deployment/assets/source/requirements.txt
python book/06-deployment/assets/source/generate_visuals.py --preview-dir .cache/section06-visuals
```

Pass `--preview-dir` followed by a directory to save 640-pixel raster previews and animation contact
sheets. From the repository root, `.cache/section06-visuals` keeps those previews out of version
control. The generation script also places Matplotlib's authoring cache under `.cache` by default.

`visual-data.json` holds the timeline allocations and illustrative plot values. It contains no
measured results from the deployment exercise. Paired percentages use each instance's current
revenue as the denominator; their arithmetic mean is 0.75%. The timeline totals 300 seconds, of
which 180 seconds are allocated to the primary solve. That is also the growth plot's budget line.

The static diagrams and GIF frames share the same drawing functions. Labels, shapes, and dashed
paths reinforce color. Every complete explanation remains available in a static figure; animation
is offered only inside an optional disclosure in the chapter.
