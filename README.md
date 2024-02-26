![Explain PostgreSQL](https://github.com/MGorkov/explain-postgresql-sublime/blob/main/images/explain-logo.png?raw=true) Explain PostgreSQL
===============

Analyzes EXPLAIN plan from PostgreSQL and related (Greenplum, Citus, TimescaleDB and Amazon RedShift).

Shows plan and node details and visualizations with piechart, flowchart and tilemap, also gives smart recommendations to improve query.

Uses the public api from the [explain.tensor.ru](https://explain.tensor.ru/api-description/) , the site can be changed in settings.

[Learn more](https://explain.tensor.ru/about)

## Features

* Beautifier and formatter for SQL <kbd>CTRL+ALT+f</kbd>
![Beautifier and formatter for SQL](https://github.com/MGorkov/explain-postgresql-sublime/blob/main/images/formatter.gif?raw=true)
* Explain Analyze for query plan <kbd>CTRL+ALT+e</kbd>
![Beautifier and formatter for SQL](https://github.com/MGorkov/explain-postgresql-sublime/blob/main/images/explainer.gif?raw=true)

## Settings

![Explain PostgreSQL settings](https://github.com/MGorkov/explain-postgresql-sublime/blob/main/images/settings.png?raw=true)

## Installing

### Using [Sublime Package Control](https://packagecontrol.io/packages/ExplainPostgreSQL)

Click the `Package Control: Install Package` menu item and choose `Explain PostgreSQL`

1. Press <kbd>CTRL+SHIFT+p</kbd>
2. Type *`Install Package`*
3. Install *`Explain PostgreSQL`*

Please install and configure the [SQLTools](https://packagecontrol.io/packages/SQLTools) plugin first.

### Download Manually

1. Download the latest released zip file [here](https://explain.tensor.ru/downloads-plugins/)
2. Unzip the files to `Explain PostgreSQL`
3. Find your `Packages` directory using the menu item  `Preferences -> Browse Packages...`
4. Copy the folder into your Sublime Text `Packages` directory
