# Business Analytics Dashboard

A simple interactive business analytics dashboard built with **Python**,
**Streamlit**, **Pandas**, and **Plotly**. It displays key business
metrics, a sales-over-time chart, a product-category donut chart,
top-product comparisons, and a recent-orders table.

> **Important:** The app currently uses randomly generated sample data
> and hard-coded KPI values. It is a demonstration dashboard, not a
> connection to live business data.

## Features

-   **Key metrics:** Total Revenue, New Customers, Sales Growth, and
    Average Order Value.
-   **Sales Overview:** A line chart of daily sample sales for the most
    recent 30-day period.
-   **Customer / product distribution:** A donut chart showing category
    values for Electronics, Fashion, Home, and Others.
-   **Top Products:** A bar chart comparing five sample products.
-   **Recent Orders:** A small table showing sample customers and order
    statuses.
-   **Sidebar controls:** Region, Product Category, and date-range
    selectors are displayed in the sidebar.

## Requirements

-   Python 3.9 or later is recommended.
-   Streamlit
-   Pandas
-   Plotly

## Installation

1.  Open a terminal.

2.  (Optional but recommended) Create and activate a virtual
    environment.

    **macOS / Linux**

    ``` bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    **Windows**

    ``` powershell
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  Install the required packages:

    ``` bash
    python -m pip install streamlit pandas plotly
    ```

## Run the dashboard

Save the Python file as `Analytics_Dashboard.py`, then run this command
from the directory containing it:

``` bash
python -m streamlit run Analytics_Dashboard.py
```

Streamlit will print a local URL in the terminal, usually
`http://localhost:8501`. Open that URL in your browser.

**Do not launch this app with Spyder's ordinary Run File / `%runfile`
command.** Streamlit apps should be launched using `streamlit run`;
running them directly can produce repeated `missing ScriptRunContext`
warnings and may prevent widgets from working as intended.

To stop the app, press `Ctrl+C` in the terminal where it is running.

## Project structure

``` text
.
├── Analytics_Dashboard.py
└── README.md
```

## Data and current limitations

-   The `sales`, `customers`, and `profits` columns are generated
    randomly each time the app starts or reruns.
-   The KPI cards display fixed example values; they are not calculated
    from the generated data.
-   The sidebar selections are currently displayed but **do not filter**
    the charts or table.
-   The donut chart uses values `[28, 44, 23, 23]`. These add up to 118,
    so if they are intended to represent percentages, review or
    normalize them.
-   The recent-orders table contains three sample customers, each with a
    `Completed` status.
-   No external database, API, or live data source is configured.

## Troubleshooting

### `missing ScriptRunContext` warnings

Run the app using:

``` bash
python -m streamlit run Analytics_Dashboard.py
```

rather than running the file directly through Spyder or a plain Python
command. If the warning remains, check that Streamlit is installed in
the same Python environment used to launch the app.

### `ModuleNotFoundError`

Install the missing package in the environment used to run Streamlit.
For example:

``` bash
python -m pip install streamlit pandas plotly
```

### Port 8501 is already in use

Choose another port:

``` bash
python -m streamlit run Analytics_Dashboard.py --server.port 8502
```

Then open the URL Streamlit prints.

### `use_container_width` deprecation warning

The current script already uses `width="stretch"` for Plotly charts. If
an older copy of the script uses `use_container_width=True`, replace it
with `width="stretch"` in supported Streamlit calls.

## Possible future improvements

-   Connect the dashboard to a verified data source.
-   Calculate KPIs from the dataset rather than hard-coding them.
-   Apply the sidebar filters to the charts and table.
-   Add validation and clear labels for units and percentages.
-   Add tests and document the supported Python and package versions.

## License

No license is specified in the provided source code. Add a license file
if you intend to distribute or publish this project.
