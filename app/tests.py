import asyncio
from django.test import TestCase, AsyncClient, override_settings
from django.core.cache import cache


@override_settings(NUMBER_CACHE_KEY="test-number")
class NumberViewTestCase(TestCase):
    def setUp(self):
        """Clear cache before each test"""
        cache.delete("test-number")

    async def test_concurrent_requests(self):
        """Test that 10 concurrent requests result in number 10"""
        client = AsyncClient()

        # Create 10 concurrent requests
        tasks = [client.get("/") for _ in range(10)]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            with self.subTest(response=response):
                self.assertEqual(response.status_code, 200)

        # Verify the final cache value is 10
        final_number = cache.get("test-number")
        self.assertEqual(final_number, 10)
