"""Check replaced stock assets and the name-only unit spec after a PA update."""
import argparse, hashlib, json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--game-root', required=True, type=Path, help='PA TITANS installation directory')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
baseline = json.loads((root/'maintenance/stock-baseline.json').read_text())
problems = []
for item in baseline['files']:
    path = args.game_root/'media'/item['stock_path']
    if not path.exists():
        problems.append('Missing stock file: '+item['stock_path'])
    elif hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        problems.append('Changed stock file: '+item['stock_path'])
unit_path = 'pa/units/land/titan_structure/titan_structure.json'
stock_path = args.game_root/'media/pa_ex1/units/land/titan_structure/titan_structure.json'
if stock_path.exists():
    stock = json.loads(stock_path.read_text())
    mod = json.loads((root/unit_path).read_text())
    if mod.pop('display_name', None) != 'Singularity':
        problems.append('Unexpected mod unit name')
    stock.pop('display_name', None)
    if mod != stock:
        problems.append('Unit spec differs from installed stock beyond display_name; refresh it before release')
if problems:
    print('\n'.join(problems))
    raise SystemExit(1)
print(f"PASS: {len(baseline['files'])} replaced stock files match build {baseline['build']}; unit differs only by name.")
