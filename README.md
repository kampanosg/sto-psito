
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://stopsito.net/img/logo.png" alt="Sto Psito Resturant Logo">
  </a>

  <h3 align="center">Sto Psito Restaurant</h3>

  <p align="center">
    The official GitHub repo of Sto Psito website
    <br />
    <a href="https://stopsito.net" target="_blank"><strong>View the website »</strong></a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Architecture</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

### Architecture
Sto Psito Restaurant uses a simple and low-cost cloud architecture.

### Front End
Since the menu and website contents are not updated in a regular basis there is no need for a fully fledged CMS, that requires servers and increases the uptime costs. Therefore, the customer-facing application has been written in vanilla HTML / CSS / Javascript and is hosted using AWS S3. Furthermore, using the Cloudflare Sto Psito is available globally without delays. 

### Back End
Sto Psito takes advantage of AWS' API Gateway, Lambda and DynamoDB features to implement a bespoke reservations system. Specifically, Lambda functions process API Gateway events to write new reservations to Dynamo. After the new reservation has been written to the DB, another lambda function handles notifying the customers and resturant via Emails and SMS. 

### Built With

* [Pure HTML / CSS / Javascript (Frontend)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [AWS Lambda (Python) / API Gateway / DynamoDB (Backend)](https://aws.amazon.com)


## Usage
If you'd like to use the λ functions for yourself, you can install the dependencies using `pip`, zip the entire directory and upload them to the AWS Lambda dashboard. 

For instance:
```sh 
$ cd lambda/notify
$ pip install -r requirements.txt -t .
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
George Kampanos - [LinkedIn](https://uk.linkedin.com/in/kampanosg) - kampanosg@outlook.com

<img src="https://stopsito.net/media/sto_psito_sunset.jpg" alt="Sto Psito Resturant Amazing Views">
