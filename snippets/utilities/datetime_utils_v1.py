#!/usr/bin/env python3
"""
日期时间工具函数

常用的日期时间操作：格式化、解析、计算差值、时区处理。
"""

from datetime import datetime, timedelta, date
from typing import Optional


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """格式化日期时间。"""
    return dt.strftime(fmt)


def parse_datetime(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> Optional[datetime]:
    """解析日期时间字符串。"""
    try:
        return datetime.strptime(date_str, fmt)
    except ValueError as e:
        print(f"日期解析失败: {e}")
        return None


def date_range(start: date, end: date) -> list:
    """
    生成日期范围列表。

    Args:
        start: 起始日期
        end: 结束日期

    Returns:
        从 start 到 end 的日期列表
    """
    delta = end - start
    return [start + timedelta(days=i) for i in range(delta.days + 1)]


def time_ago(dt: datetime) -> str:
    """
    计算某个时间距离现在的时间差，返回人类可读的字符串。

    Args:
        dt: 过去的时间点

    Returns:
        类似 "3天前"、"2小时前" 的字符串
    """
    now = datetime.now()
    diff = now - dt

    seconds = diff.total_seconds()
    if seconds < 60:
        return f"{int(seconds)}秒前"
    elif seconds < 3600:
        return f"{int(seconds / 60)}分钟前"
    elif seconds < 86400:
        return f"{int(seconds / 3600)}小时前"
    elif seconds < 2592000:
        return f"{int(seconds / 86400)}天前"
    else:
        return f"{int(seconds / 2592000)}个月前"


def get_weekday_name(dt: date) -> str:
    """获取星期几的中文名称。"""
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return weekdays[dt.weekday()]


if __name__ == "__main__":
    now = datetime.now()
    print(f"当前时间: {format_datetime(now)}")

    parsed = parse_datetime("2024-01-15 10:30:00")
    if parsed:
        print(f"解析结果: {format_datetime(parsed)}")
        print(f"距今: {time_ago(parsed)}")
        print(f"星期: {get_weekday_name(parsed.date())}")

    start = date(2024, 1, 1)
    end = date(2024, 1, 7)
    print(f"\n日期范围 ({start} ~ {end}):")
    for d in date_range(start, end):
        print(f"  {d} ({get_weekday_name(d)})")
