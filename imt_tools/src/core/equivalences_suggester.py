from src.core.promt import Promt


class EquivalencesSuggester(Promt):
    """A class to disambiguate specific acronyms to expand the actual concept of the word.  For example, "adt" in the context of Cancer research refers to "Androgen Deprivation Therapy". 
    """

    def __init__(
        self,
        model: str,
        temperature: float = 0.2,
        max_tokens: int = 1000,
        frequency_penalty: float = 0.0
    ) -> None:
        """Initialise the EquivalencesSuggester class.

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

        example_1 = ('adt', 'Cancer Research', 'Androgen Deprivation Therapy')

        # Set the parameters for the OpenAI model
        self.parameters = {
            "model": model,
            "messages": [
                {"role": "system", "content": f"You are a helpful assistant trained on the task of disambiguating acronyms in a certain context. For example, if I give you the word {example_1[0]} in the context of {example_1[1]}, you will give me the disambiguated word {example_1[2]}. Just answer with the disambiguated word, no need to write anything else."
                 },
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "frequency_penalty": frequency_penalty
        }

    def get_dis(
            self,
            acronym: str,
            context: str) -> str:
        """Get the disambiguated word for a specific acronym in a specific context.

        Parameters
        ----------
        acronym : str
            The acronym to disambiguate.
        context : str
            The context of the acronym.

        Returns
        -------
        str
            The disambiguated word.
        """

        gpt_prompt = f"Disambiguate this acronym: {acronym} in the context of {context}"
        return self._promt(gpt_prompt)

    def get_dis_list(
        self,
        acronyms: list,
        context: str
    ) -> list:
        """Get the disambiguated word for a list of acronyms in a specific context.

        Parameters
        ----------
        acronyms : list
            A list of acronyms to disambiguate.
        context : str
            The context of the acronyms.

        Returns
        -------
        list
            A list of disambiguated words.
        """

        gpt_prompt = f"Disambiguate each of the following acronyms in the context of {context} and return it as a Python list with the disambiguated words: {acronyms}"
        return eval(self._promt(gpt_prompt))
