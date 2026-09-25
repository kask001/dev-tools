#!/usr/bin/env python3
"""
建造者模式 (Builder Pattern)

将一个复杂对象的构建与它的表示分离，使得同样的构建过程
可以创建不同的表示。

示例：构建一个 SQL 查询语句。
"""


class QueryBuilder:
    """SQL 查询构建器。"""

    def __init__(self, table: str):
        self._table = table
        self._select = "*"
        self._where: list = []
        self._order_by: str = ""
        self._limit: int = 0
        self._offset: int = 0

    def select(self, *columns: str) -> 'QueryBuilder':
        """设置查询字段。"""
        self._select = ", ".join(columns) if columns else "*"
        return self

    def where(self, condition: str) -> 'QueryBuilder':
        """添加 WHERE 条件。"""
        self._where.append(condition)
        return self

    def order_by(self, column: str, direction: str = "ASC") -> 'QueryBuilder':
        """设置排序。"""
        self._order_by = f"ORDER BY {column} {direction}"
        return self

    def limit(self, count: int) -> 'QueryBuilder':
        """设置返回数量。"""
        self._limit = count
        return self

    def offset(self, count: int) -> 'QueryBuilder':
        """设置偏移量。"""
        self._offset = count
        return self

    def build(self) -> str:
        """构建最终的 SQL 语句。"""
        sql = f"SELECT {self._select} FROM {self._table}"

        if self._where:
            sql += f" WHERE {' AND '.join(self._where)}"

        if self._order_by:
            sql += f" {self._order_by}"

        if self._limit:
            sql += f" LIMIT {self._limit}"

        if self._offset:
            sql += f" OFFSET {self._offset}"

        return sql + ";"


if __name__ == "__main__":
    query = (
        QueryBuilder("users")
        .select("name", "email", "age")
        .where("age >= 18")
        .where("status = 'active'")
        .order_by("name")
        .limit(10)
        .offset(20)
    )
    print(query.build())

    simple = QueryBuilder("products").where("price < 100").order_by("price", "DESC")
    print(simple.build())
