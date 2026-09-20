"""Create installable .rpp ZIPs from examples/plugins."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]; out=root/'dist'/'plugins'; out.mkdir(parents=True,exist_ok=True)
for plugin in (root/'examples'/'plugins').iterdir():
    if plugin.is_dir() and (plugin/'manifest.json').exists():
        with ZipFile(out/(plugin.name+'.rpp'),'w',ZIP_DEFLATED) as z:
            for p in plugin.rglob('*'):
                if p.is_file(): z.write(p,p.relative_to(plugin))
