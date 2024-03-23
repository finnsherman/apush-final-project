import "./APUSH.css"
import { Link } from "react-router-dom";
import * as React from "react";

function Title() {
    return (
        <html lang="en-US">

            <head>
                <p class="title" id="title">Democracy, Republicanism and Self Determination</p>
            </head>

            <body>
                <div>
                    <p class="selector1" id="s1">Early roots</p>
                    <button class="button" onclick="document.location='EarlyRoots.html'">Learn more...</button>

                    <p class="selector2" id="s2">The First Experiment</p>
                    <button class="button" onclick="document.location='FirstExperiment.html'">Learn more...</button>

                    <p class="selector3" id="s3">Refining the Republic</p>
                    <button class="button" onclick="document.location='Refining.html'">Learn more...</button>
                </div>

            </body>
                <Link to="/Refining">New Stand Form</Link>
        </html>
    );
}
export default Title