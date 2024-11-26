from typing import Union


async def get_report_message_text(crm_data: list[dict[str, Union[str, int]]]) -> str:
    if not crm_data:
        return "📊 Daily revenue report:\n No matching leads"
    text = "📊 Daily Revenue Report:\n"
    for manager_data in crm_data:
        text += f"👤 Manager ID: {manager_data.get('manager_id')} 💰 Revenue: {manager_data.get('total_revenue')}\n"
    return text

