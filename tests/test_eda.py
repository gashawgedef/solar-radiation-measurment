import pytest
import pandas as pd
from src.eda_analysis import summarize_statistics


def test_summarize_statistics():
    data = {"GHI": [10, 20, 30], "DNI": [5, 10, 15]}
    df = pd.DataFrame(data)
    summary = summarize_statistics(df)
    assert "mean" in summary.index
    assert summary.loc["mean", "GHI"] == 20
