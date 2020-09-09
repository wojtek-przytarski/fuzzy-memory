import {BASE_URL} from "./consts";

export const JobResultService = {
    fetch(jobId) {
        const url = `${BASE_URL}/second-tetration/${jobId}`;
        return new Promise((resolve, reject) => {
                fetch(url).then(response => response.json())
                    .then(data => {
                            resolve(data.result)
                        }
                    ).catch(error => reject(error.detail))
            }
        )
    }
}
