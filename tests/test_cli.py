from click.testing import CliRunner
from docforge.cli import cli

def test_cli_extract():
    runner = CliRunner()
    res = runner.invoke(cli, ["extract", "Patient has diabetes"])
    assert res.exit_code == 0
    assert "E11.9" in res.output

def test_cli_bench():
    runner = CliRunner()
    res = runner.invoke(cli, ["bench"])
    assert res.exit_code == 0
    assert "91.4" in res.output
