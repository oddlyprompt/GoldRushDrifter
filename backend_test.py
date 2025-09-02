#!/usr/bin/env python3
"""
Backend API Test for Gold Rush Drifter Game
Note: This game is a frontend-only application with no backend dependencies.
Testing the existing backend APIs for completeness.
"""

import requests
import sys
from datetime import datetime

class SimpleAPITester:
    def __init__(self, base_url="https://gunslinger-mud.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0

    def run_test(self, name, method, endpoint, expected_status, data=None):
        """Run a single API test"""
        url = f"{self.base_url}/api/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                if response.content:
                    try:
                        json_data = response.json()
                        print(f"   Response: {json_data}")
                    except:
                        print(f"   Response: {response.text[:100]}")
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"   Response: {response.text[:200]}")

            return success, response.json() if success and response.content else {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test root API endpoint"""
        return self.run_test("Root API", "GET", "", 200)

    def test_create_status_check(self):
        """Test creating a status check"""
        test_data = {"client_name": f"test_client_{datetime.now().strftime('%H%M%S')}"}
        return self.run_test("Create Status Check", "POST", "status", 200, test_data)

    def test_get_status_checks(self):
        """Test getting status checks"""
        return self.run_test("Get Status Checks", "GET", "status", 200)

def main():
    print("🎮 Gold Rush Drifter - Backend API Testing")
    print("=" * 50)
    print("Note: This is a frontend-only game with no backend dependencies.")
    print("Testing existing backend APIs for completeness.\n")
    
    # Setup
    tester = SimpleAPITester()

    # Run tests
    print("🔧 Testing Backend APIs...")
    
    # Test root endpoint
    tester.test_root_endpoint()
    
    # Test status check creation
    tester.test_create_status_check()
    
    # Test status check retrieval
    tester.test_get_status_checks()

    # Print results
    print(f"\n📊 Backend API Test Results:")
    print(f"   Tests passed: {tester.tests_passed}/{tester.tests_run}")
    
    if tester.tests_passed == tester.tests_run:
        print("✅ All backend APIs are working correctly")
        print("\n🎮 Game Analysis:")
        print("   - Gold Rush Drifter is a frontend-only game")
        print("   - Uses Zustand for state management")
        print("   - No backend API dependencies")
        print("   - All game logic runs in the browser")
        return 0
    else:
        print("❌ Some backend APIs failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())