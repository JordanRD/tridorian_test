from .api_client import APIClient
from ..constants import FMP_API_KEY, FMP_URL
import asyncio
import inspect


def init_fmp_request():
    return APIClient(base_url=FMP_URL, params={"apikey": FMP_API_KEY})


def with_compound_tools(tools: list):
    async def compound_tools(tools_config: list[dict]) -> list:
        """
        Description:
          Always use this tool when you need to execute multiple tools that can be executed in parallel.
        Input:
          tools_config (list): Array of dicts containing tool name and arguments dict.
              Format: [{"tool_name": "tool_name", "args": {arg1: value1, arg2: value2}}, ...]
        Output:
          A list of results from each tool execution in order.
        """
        print(tools_config)
        results = []
        tools_dict = {
            tool.__name__: tool for tool in tools if tool.__name__ != "compound_tools"
        }

        for config in tools_config:
            print(config)
            tool_name = config["tool_name"].split(".")[-1]
            if tool_name in tools_dict:
                result = tools_dict[tool_name](**config["args"])
                if inspect.isawaitable(result):
                    # true async task
                    results.append(asyncio.create_task(result))
                else:
                    # sync result already computed — wrap it so it doesn't block
                    results.append(asyncio.to_thread(lambda r=result: r))

        return await asyncio.gather(*results)

    tools.append(compound_tools)
    return tools
