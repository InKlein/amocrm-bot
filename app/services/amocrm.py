from collections import defaultdict
from datetime import datetime, timezone
from typing import Union

from amocrm.v2 import Lead


async def fetch_revenue_data() -> list[dict[str, Union[str, int]]]:
    leads = Lead.objects.all()
    revenue_by_manager: dict[str, int] = defaultdict(int)

    today = datetime.now(timezone.utc).date()
    for lead in leads:
        if lead.is_deleted is False and lead.closed_at:
            closed_date = lead.closed_at.date()
            if closed_date == today:
                manager_id = lead.responsible_user.id
                revenue_by_manager[manager_id] += lead.price

    return [
        {"manager_id": manager_id, "total_revenue": revenue}
        for manager_id, revenue in revenue_by_manager.items()
    ]

