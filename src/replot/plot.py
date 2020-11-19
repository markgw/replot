import os
import pickle
import traceback
import warnings
from pathlib import Path


def plot(output_path, plotting_code, data, raise_plotting_errors=False):
    """

    Writes to ``output_path``: ``data.pkl``, ``plot.py``, plus any files that get
    produced when the plotting code is executed (typically a plot, at least).

    :param raise_plotting_errors: By default (False), any errors encountered during
        plotting lead to warnings and are not raised, since you can go and fix the
        plotting code directly in the output files if you want. If True, raise errors
    :param data: All data needed for producing plots, as a dictionary. This is pickled
        and can easily be loaded from your plotting code using ``replot.get_data()``,
        or just unpickling ``data.pkl`` in the current directory.
    :param plotting_code: A pathlib.Path to a Python file containing the plotting code,
        or a string containing the code. If a string with no linebreaks is given, it
        is assumed to be a path
    :param output_path: Path to a directory where the output files will be written.
    :return:
    """
    plotting_code_str = None
    if isinstance(plotting_code, str):
        if "\n" in plotting_code:
            # Code as a string
            plotting_code_str = plotting_code
        else:
            # Path as a string
            plotting_code = Path(plotting_code)
    if isinstance(plotting_code, Path):
        # Read in the plotting code from this path
        with plotting_code.open("r") as f:
            plotting_code_str = f.read()
    if plotting_code_str is None:
        raise TypeError("plotting_code should be a string path, string containing code or a Path object")

    # Output the plotting code
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    plot_path = os.path.join(output_path, "plot.py")
    with open(plot_path, "w") as f:
        f.write(plotting_code_str)

    # Output the data
    with open(os.path.join(output_path, "data.pkl"), "wb") as f:
        pickle.dump(data, f)

    # Now try calling the plotting code so we produce the plots straight away
    # Change working directory to the one containing the script
    old_cwd = os.getcwd()
    os.chdir(output_path)
    # Execute the python script: we already have this as a string
    try:
        exec(plotting_code_str, locals(), locals())
    except Exception as e:
        if raise_plotting_errors:
            raise
        else:
            warnings.warn("error executing plotting code: {}. {}. Code in {}".format(e, traceback.format_exc(), plot_path))
    # Change working dir back
    os.chdir(old_cwd)
