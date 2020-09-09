import {JobResultService} from "./job-result.service";
import {BASE_URL} from "./consts";

export const SecondTetrationService = {
    fetch(number) {
        const url = `${BASE_URL}/second-tetration/`;
        const requestOptions = {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({number})
        };

        return new Promise((resolve, reject) => {
            fetch(url, requestOptions).then(response => response.json())
                .then(data => {
                    if (data.result) {
                        resolve(data.result)
                    } else if (data.job_id) {
                        let count = 0;
                        let waitForJobResult = () => {
                            count++;
                            JobResultService.fetch(data.job_id).then(result => {
                                if (result) {
                                    resolve(result);
                                } else {
                                    if (count > 10) {
                                        reject("Could not calculate the result, please try again later")
                                    } else {
                                        let timeout = Math.min(50 * (2 ** count), 2000);  // wait longer after every request, up to 2 seconds
                                        setTimeout(waitForJobResult, timeout);
                                    }
                                }
                            });

                        }
                        waitForJobResult();
                    }
                }).catch(err => reject(err));
        })
    }
}
