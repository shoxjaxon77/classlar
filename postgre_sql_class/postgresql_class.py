from asyncpg import create_pool
import asyncio

class PostgreSql:
    def __init__(self):
        self.path = None
    
    async def create(self):
        self.pool = await create_pool(
            host = "localhost",
            user = "postgres",
            password = "shokh",
            database = "postgres"
        ) 

    async def ishlatish(self,sql,fetch=False,fetchval=False,fetchrow=False,execute=False):
        async with self.pool.acquire() as con:
            async with con.transaction():
                if fetch:
                    data = await con.fetch(sql)
                if fetchval:
                    data = await con.fetchval(sql)
                if fetchrow:
                    data = await con.fetchrow(sql)
                if execute:
                    data = await con.execute(sql)
                return data
        
    async def uquvchilar(self):
        try:
            sql = "SELECT * FROM uquvchilar"
            return await self.ishlatish(sql,fetch = True)
        except Exception as a:
            return f"{a}"
    
    async def uquvchi_id(self,ism,familiya):
        try:
            sql = f"SELECT id FROM uquvchilar WHERE ism = '{ism}' AND familiya = '{familiya}'"
            return await self.ishlatish(sql,fetchval=True)
        except Exception as a:
            return f"{a}"
    
    async def id_uquvchi(self,id):
        try:
            sql = f"SELECT * FROM uquvchilar WHERE id = {id}"
            return await self.ishlatish(sql,fetchrow=True)
        except Exception as a:
            return f"{a}"
    
    async def change_ism(self,old_ism,new_ism):
        try:
            sql = f"UPDATE uquvchilar SET ism = '{new_ism}' WHERE ism = '{old_ism}'"
            await self.ishlatish(sql,execute=True)
        except Exception as a:
            return f"{a}"

async def test():
    base = PostgreSql()
    await base.create()
    
    print("Barcha oquvchilar:",'\n',await base.uquvchilar(),'\n')

    print("Berilgan o'quvchining id si:",'\n',await base.uquvchi_id("Umida","Tajiyeva"),'\n')

    print("Berilgan id dagi o'quvchining ma'lumotlari:",'\n',await base.id_uquvchi(2),'\n')

    await base.change_ism("Abror","Abrorbek")
    
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(test())