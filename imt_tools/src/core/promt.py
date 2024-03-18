import os
import openai


class Promt(object):

    def __init__(self) -> None:
        try:
            openai.api_key = os.environ["OPENAI_API_KEY"]
        except KeyError:
            raise Exception(
                "Please set the OPENAI_API_KEY environment variable.")

    def set_parameters(self, **kwargs) -> None:
        """Set parameters for the OpenAI model.

        Parameters
        ----------
        **kwargs : dict
            A dictionary of parameters to set.
        """

        for key, value in kwargs.items():
            if key != "messages":
                self.parameters[key] = value
                
    def update_messages(
        self,
        messages: list
    ) -> None:
        """Update the messages of the OpenAI model, always keeping the first message (i.e., the system role)
        
        Parameters
        ----------
        messages : list
            A list of messages to update the model with.
        """

        self.parameters["messages"] = [
            self.parameters["messages"][0], *messages]

        return

    def _promt(self, gpt_prompt) -> str:
        """Promt the OpenAI ChatCompletion model with a message.
        
        Parameters
        ----------
        gpt_prompt : str
            A message to promt the model with.
        
        Returns
        -------
        str
            The response of the OpenAI model.
        """

        message = [{"role": "user", "content": gpt_prompt}]
        self.update_messages(message)
        response = openai.ChatCompletion.create(
            **self.parameters
        )
        return response["choices"][0]["message"]["content"]
