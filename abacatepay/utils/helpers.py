from pydantic import BaseModel


def prepare_data(data, model_cls: type[BaseModel], *, use_alias: bool = True) -> dict:
    """It formats the data to be in compliance with the given model class to be sent to the API

    Args:
        data (BaseModel | dict): the user input data.
        model_cls (type[BaseModel]): the model that will dumps.
        use_alias (bool, optional): if `True` dumps by alias. Defaults to True.
    """
    if isinstance(data, model_cls):
        validated_data = data.model_dump(by_alias=use_alias)
        return {k: v for k, v in validated_data.items() if v != {}}

    elif isinstance(data, dict):
        validated_data = model_cls.model_validate(data).model_dump(by_alias=use_alias)
        return {k: v for k, v in validated_data.items() if v != {}}

    raise TypeError('Invalid data type.')

