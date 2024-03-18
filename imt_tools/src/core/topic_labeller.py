from src.core.promt import Promt


class TopicLabeller(Promt):
    """A class to label chemical descriptions with topics.
    """

    def __init__(
        self,
        model: str,
        temperature: float = 0.2,
        max_tokens: int = 1000,
        frequency_penalty: float = 0.0
    ) -> None:
        """Initialise the TopicLabeller class.

        Parameters
        ----------
        model : str
            The OpenAI model to use.
        temperature : float, optional
            The temperature of the OpenAI model, by default 0.2
        max_tokens : int, optional
            The maximum number of tokens to use, by default 1000
        frequency_penalty : float, optional
            The frequency penalty of the OpenAI model, by default 0.0
        """

        super().__init__()

        example_1 = ('network, traffic, vehicle, energy, communication, service, deep, reinforcement, sensor, wireless, road, channel, management, node, UAV',
                     'Traffic Management and Autonomous Driving')

        # Set the parameters for the OpenAI model
        self.parameters = {
            "model": model,
            "messages": [
                {"role": "system", "content": f"You are a helpful assistant trained on the task of labelling chemical descriptions of the topics of a certain topic model. For example, if I give you the chemical description {example_1[0]}, you will give me the label {example_1[1]}. Just answer with the label, no need to write anything else."
                 },
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "frequency_penalty": frequency_penalty
        }

    def get_label(self, chem_desc: str) -> str:
        """Get a label for a chemical description.

        Parameters
        ----------
        chem_desc : str
            A chemical description.

        Returns
        -------
        str
            A label for the chemical description.
        """

        gpt_prompt = f"Give me a label for this set of words: {chem_desc}"
        return self._promt(gpt_prompt)

    def get_labels(self, chem_descs: list) -> list:
        """Get labels for a list of chemical descriptions.

        Parameters
        ----------
        chem_descs : list
            A list of chemical descriptions.

        Returns
        -------
        list
            A list of labels for the chemical descriptions.
        """

        gpt_prompt = f"Give me a label for each of the following set of words and return it as a Python list with the labels: {chem_descs}"
        return eval(self._promt(gpt_prompt))
