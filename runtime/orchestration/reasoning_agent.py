import asyncio

from runtime.llm_runtime import LLMRuntime

runtime = LLMRuntime()

async def run_reasoning(task):

    prompt = f"""

    Analyze:

    {task}

    Return:
    - risks
    - optimization
    - orchestration
    - governance analysis

    """

    result = await runtime.generate(prompt)

    print()
    print("=" * 70)
    print("REASONING AGENT OUTPUT")
    print("=" * 70)

    for k,v in result.items():

        print(k, "=>", v)

asyncio.run(

    run_reasoning(

        "Optimize governed cognitive runtime"

    )

)
