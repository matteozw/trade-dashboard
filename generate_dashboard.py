
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Trade Signals Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .container {
                width: 80%;
                margin: auto;
                overflow: hidden;
            }
            header {
                background: #333;
                color: #fff;
                padding-top: 30px;
                min-height: 70px;
                border-bottom: #0779e4 3px solid;
            }
            header a {
                color: #fff;
                text-decoration: none;
                text-transform: uppercase;
                font-size: 16px;
            }
            header ul {
                padding: 0;
                list-style: none;
            }
            header li {
                float: left;
                display: inline;
                padding: 0 20px 0 20px;
            }
            header #branding {
                float: left;
            }
            header #branding h1 {
                margin: 0;
            }
            header nav {
                float: right;
                margin-top: 10px;
            }
            section {
                padding: 20px;
                margin-top: 20px;
                background: #fff;
            }
            footer {
                padding: 20px;
                margin-top: 20px;
                color: #fff;
                background-color: #333;
                text-align: center;
            }
            .chart {
                width: 100%;
                height: 400px;
                margin: 20px 0;
                background: #e2e2e2;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #333;
                font-size: 24px;
            }
        </style>
    </head>
    <body>
        <header>
            <div class="container">
                <div id="branding">
                    <h1>Trade Signals Dashboard</h1>
                </div>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Signals</a></li>
                        <li><a href="#">Charts</a></li>
                        <li><a href="#">Performance</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <section id="signals">
            <div class="container">
                <h2>Daily Trade Signals - 2025-05-15</h2>
                <h3>XAU/USD</h3>
                <p>Buy Signal: Entry at $3,286.54, Stop-Loss at $3,278.85, Take-Profit at $3,300.00</p>
                <p>Risk/Reward Ratio: 1.86</p>
                <div class="chart">XAU/USD Chart Placeholder</div>

                <h3>JPY/EUR</h3>
                <p>Buy Signal: Entry at ¥164.50, Stop-Loss at ¥163.00, Take-Profit at ¥167.00</p>
                <p>Risk/Reward Ratio: 2.00</p>
                <div class="chart">JPY/EUR Chart Placeholder</div>

                <h3>EUR/CHF</h3>
                <p>Buy Signal: Entry at 1.0835, Stop-Loss at 1.0800, Take-Profit at 1.0900</p>
                <p>Risk/Reward Ratio: 1.86</p>
                <div class="chart">EUR/CHF Chart Placeholder</div>

                <h3>NZD/CHF</h3>
                <p>Buy Signal: Entry at 0.6050, Stop-Loss at 0.6000, Take-Profit at 0.6150</p>
                <p>Risk/Reward Ratio: 2.00</p>
                <div class="chart">NZD/CHF Chart Placeholder</div>
            </div>
        </section>

        <footer>
            <p>Trade Signals Dashboard &copy; 2025</p>
        </footer>
    </body>
    </html>
    