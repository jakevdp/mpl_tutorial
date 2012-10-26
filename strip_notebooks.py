import json
import copy
import os


def strip_notebook(filename, marker='###',
                   outfile_live=None, outfile_clean=None):
    if not filename.endswith('.ipynb'):
        import warnings
        warnings.warn('%s not a notebook file' % filename)
        return

    if outfile_live is None:
        outfile_live = os.path.splitext(filename)[0] + '_live.ipynb'

    if outfile_clean is None:
        outfile_clean = os.path.splitext(filename)[0] + '_clean.ipynb'

    F = json.load(open(filename, 'r'))

    F1 = copy.deepcopy(F)
    F2 = copy.deepcopy(F)

    for i, worksheet in enumerate(F['worksheets']):
        if 'cells' not in worksheet:
            continue

        for j, cell in enumerate(worksheet['cells']):
            if 'input' not in cell:
                continue

            cell_input = cell['input']

            if (len(cell_input) > 0) and (cell_input[0].startswith(marker)):
                F1['worksheets'][i]['cells'][j]['input'] = cell_input[1:]

                F2['worksheets'][i]['cells'][j]['input'] = []
                F2['worksheets'][i]['cells'][j]['outputs'] = []

    json.dump(F1, open(outfile_clean, 'w'))
    json.dump(F2, open(outfile_live, 'w'))


def main():
    if not os.path.exists('notebooks'):
        os.makedirs('notebooks')

    if not os.path.exists('notebooks_ex'):
        os.makedirs('notebooks_ex')

    for f in os.listdir('notebooks_raw'):
        f_raw = os.path.join('notebooks_raw', f)
        f_clean = os.path.join('notebooks', f)
        f_live = os.path.join('notebooks_ex', f)
        
        strip_notebook(f_raw,
                       outfile_clean=f_clean,
                       outfile_live=f_live)

if __name__ == '__main__':
    main()
