<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/shreyasdatta/e-Commerce-chatbot-rasa">
    <img src="https://media.discordapp.net/attachments/309638610909396993/999559527194177556/OwlBot.png?width=819&height=657" alt="Logo" width="95" height="80">
  </a>

<h3 align="center">e-Commerce Chatbot</h3>

  <p align="center">
    Powered by <b>Rasa Open Source</b> | To assist in e-commerce support conversations
    <br />
    <a href="https://rasa.com/docs/rasa/glossary"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/shreyasdatta/e-Commerce-chatbot-rasa">View Demo</a>
    ·
    <a href="https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/issues">Report Bug</a>
    ·
    <a href="https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![e-Commerce_chatbot](https://i.imgur.com/bnAOaY1.png)

A chatbot capable of reading, deciphering intents from user messages, and output appropriate responses based on it.

Assist in searching for products and narrowing down searches through conversations.

Place orders and track the status of an order.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* Rasa Open Source 3.1
* [![Rasa][Python.js]][Python-url]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Install rasa 3.1.1
    ```sh
    pip3 install rasa==3.1.1
    ```
* Install python 3.7.0+

* Create a new virtual environment by choosing a Python interpreter[v.3.7.9] and making a ./venv directory to hold it
    ```sh
    python3 -m venv ./venv
    ```
* Activate virtual env
  ```sh
  source ./venv/bin/activate
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/shreyasdatta/e-Commerce-chatbot-rasa.git
   ```
2. Activate virtual env

3. Mount the model `(models/20220716-025700-trusting-normal.tar.gz)`

4. Run the rasa shell command
    ```sh
    rasa shell
    ```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [X] hold basic greet-happy-path conversations
- [X] user can inquire about bot capabilities
- [X] user can inquire about search techniques
- [X] bot guides through search process
    - [X] query user for search term
    - [X] bot suggests search terms
    - [X] multi-field querying (for this example, in our deployed database the bot queries from the following columns)
        - column: ProductRoles
        - column: ProductCategory
- [X] place an order on confirmed product choice
    - [X] update Order table with unique order id and user_id from tracker
- [X] check for order status

See the [pull requests](https://github.com/ShreyasDatta/e-Commerce-chatbot-rasa/pull/1) for a full list of proposed features and task completion roadmap.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Shreyas Datta - [@FirePhoenix837](https://twitter.com/FirePhoenix837) - yasdatta@gmail.com

Project Link: [https://github.com/shreyasdatta/e-Commerce-chatbot-rasa](https://github.com/shreyasdatta/e-Commerce-chatbot-rasa)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[contributors-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[forks-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/network/members
[stars-shield]: https://img.shields.io/github/stars/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[stars-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/stargazers
[issues-shield]: https://img.shields.io/github/issues/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[issues-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/issues
[license-shield]: https://img.shields.io/github/license/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[license-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ShreyasDatta
<!-- [product-screenshot]: https://i.imgur.com/bnAOaY1.png -->

[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/

[Python.js]: https://img.shields.io/pypi/pyversions/python?logoColor=%09%238B7D6B&style=for-the-badge
[Python-url]: https://www.python.org/downloads/release/python-379/
