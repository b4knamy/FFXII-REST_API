from django.test import TestCase
from .models import Character, Esper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Create your tests here.
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
time_wait_answer = 1.5

class ApiGetCharacters(TestCase):

    def setUp(self):

        """ CREATING ALL CHARACTER TEST DATABASE"""

        Character.objects.create(name='Vaan', race='Human', hometown='Rabanastre', age='17', char_type='Principal')
        Character.objects.create(name='Balthier', race='Human', hometown='Archades', age='22', char_type='Principal')
        Character.objects.create(name='Basch', race='Human', hometown='Republic of Landis', age='36', char_type='Principal')
        Character.objects.create(name='Ashe', race='Human', hometown='Rabanastre', age='19', char_type='Principal')
        Character.objects.create(name='Penelo', race='Human', hometown='Rabanastre', age='16', char_type='Principal')
        Character.objects.create(name='Fran', race='Viera', hometown='Eruyt village', age='Unknow', char_type='Principal')
        Character.objects.create(name='Vossler', race='Human', hometown='Rabanastre', age='38', char_type='Guest')
        Character.objects.create(name='Reddas', race='Human', hometown='Unknow', age='33', char_type='Guest')
        Character.objects.create(name='Reks', race='Human', hometown='Rabanastre', age='17', char_type='Guest')
        Character.objects.create(name='Larsa', race='Human', hometown='Archades', age='12', char_type='Guest')
        Character.objects.create(name='Vayne', race='Human', hometown='Archadia', age='27', char_type='Antagonist')
        Character.objects.create(name='Venat', race='Occuria', hometown='Unknow', age='Unknow', char_type='Antagonist')
        Character.objects.create(name='Cid', race='Human', hometown='Archadia', age='58', char_type='Antagonist')

        


    def test_getting_all_char(self):
        """CHECKING IF ALL CHARACTERS ARE BEING TAKEN CORRECTLY."""

        max_char = Character.objects.all().count()
        self.assertEquals(max_char, 13)

    def test_getting_char_by_race(self):
        """CHECKING IF ALL RACES ARE BEING TAKEN CORRECTLY"""
        races =  ['human', 'viera', 'occuria']
        all_race = [True if Character.objects.filter(race=race.capitalize()) else False for race in races]
        true_list = [True, True, True]
        self.assertEquals(all_race, true_list)


    def test_getting_char_by_hometown(self):
        """CHECKING IF ALL CHARACTERS ARE BEING TAKEN BY HOMETOWN CORRECTLY."""

        hometowns = ['rabanastre', 'archades','eruyt village', 'archadia', 'unknow']

        all_hometowns = [True if Character.objects.filter(hometown=home.capitalize()) else False for home in hometowns]
        true_list = [True, True, True, True, True]

        self.assertEquals(all_hometowns, true_list)

    def test_getting_char_by_char_type(self):
        """CHECKING IF ALL CHARACTERS ARE BEING TAKEN BY CHAR_TYPE CORRECTLY."""

        char_types = ['antagonist', 'principal','guest']

        all_char_types = [True if Character.objects.filter(char_type=c_type.capitalize()) else False for c_type in char_types]
        true_list = [True, True, True]

        self.assertEquals(all_char_types, true_list)

    def test_get_all_chars_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST ALL CHARACTERS USING SELENIUM | URL: characters/all"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/all')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_char_by_name(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST CHAR BY NAME  CHARACTER USING SELENIUM | URL: characters/filter?name=vaan"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?name=vaan')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_char_by_race(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST CHAR BY RACE  CHARACTER USING SELENIUM | URL: characters/filter?race=human"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?race=human')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_char_by_hometown(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST CHAR BY HOMETOWN CHARACTER  USING SELENIUM | URL: characters/filter?hometown=archades"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?hometown=archades')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')
    
    def test_get_char_by_age(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST CHAR BY AGE CHARACTER  USING SELENIUM | URL: characters/filter?age=17"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?age=17')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_char_by_char_type(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST CHAR BY CHAR_TYPE  CHARACTER USING SELENIUM | URL: characters/filter?char_type=antagonist"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?char_type=antagonist')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_char_with_limit(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST LIMIT 2 PARAM CHARACTER  USING SELENIUM | URL: characters/filter?hometown=Rabanastre&limit=3"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?hometown=rabanastre&limit=3')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_char_with_limit_zero(self):
        """CHECKING IF THE RETURN IS EQUAL TO 411 | TEST LIMIT=0  2 PARAM  CHARACTER USING SELENIUM | URL: characters/filter?hometown=rabanastre&limit=0"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?hometown=Rabanastre&limit=0')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '411')

    def test_get_char_with_limit_str(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT STR 2 PARAM CHARACTER  USING SELENIUM | URL: characters/filter?hometown=rabanastre&limit=error"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?hometown=Rabanastre&limit=error')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')
    def test_get_char_with_limit_parameter_error(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT WRONG WRITED 2 PARAM CHARACTER  USING SELENIUM | URL: characters/filter?hometown=rabanastre&limited=2"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/filter?hometown=Rabanastre&limited=2')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')

    def test_get_all_char_with_limit(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST LIMIT  1 PARAM USING  CHARACTER SELENIUM | URL: characters/filter?all?limit=3"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/all?limit=3')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_all_char_with_limit_str(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT STR 1 PARAM CHARACTER  USING SELENIUM | URL: characters/filter?all?limit=error"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/all?limit=error')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')

    def test_get_all_char_with_limit_zero(self):
        """CHECKING IF THE RETURN IS EQUAL TO 411 | TEST LIMIT=0 1 PARAM CHARACTER  USING SELENIUM | URL: characters/filter?all?limit=0"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/all?limit=0')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '411')

    def test_get_all_char_with_limit_parameter_error(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT WRONG WRITED 1 PARAM CHARACTER USING SELENIUM | URL: characters/filter?all?limited=2"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('characters/all?limited=2')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')
    







class ApiGetEspers(TestCase):

    def setUp(self):
        """ CREATING ALL ESPER TEST DATABASE """
        Esper.objects.create(name_esper='Zodiark', name='Zodiark, Keeper of Precepts', sign='Ophiuchus, the Snake Bearer', element='Darkness')
        Esper.objects.create(name_esper='Belias', name='Belias, the Gigas', sign='Aries, the Ram', element='Fire')
        Esper.objects.create(name_esper='Zalera', name='Zalera, the Death Seraph', sign='Gemini, the Twins', element='Death')
        Esper.objects.create(name_esper='Zeromus', name='Zeromus, the Condemner', sign='Cancer, the Crab', element='Gravity')
        Esper.objects.create(name_esper='Adrammelech', name='Adrammelech, the Wroth', sign='Capricorn, the Goat', element='Lightning')
        Esper.objects.create(name_esper='Shemhazai', name='Shemhazai, the Whisperer', sign='Sagittarius, the Archer', element='Soul')
        Esper.objects.create(name_esper='Chaos', name='Chaos, Walker of the Wheel', sign='Tauros, the Bull', element='Wind')
        Esper.objects.create(name_esper='Ultima', name='Ultima, the High Seraph', sign='Gemini, the Twins', element='Holy')
        Esper.objects.create(name_esper='Cuchulainn', name='Cúchulainn, the Impure', sign='Scorpio, the Scorpion', element='Poison')
        Esper.objects.create(name_esper='Hashmal', name='Hashmal, Bringer of Order', sign='Leo, the Lion', element='Earth')
        Esper.objects.create(name_esper='Mateus', name='Mateus, the Corrupt', sign='Pisces, the Fish', element='Ice')
        Esper.objects.create(name_esper='Famfrit', name='Famfrit, the Darkening Cloud', sign='Aquarius, the Water Bearer', element='Water')
        Esper.objects.create(name_esper='Exodus', name='Exodus, the Judge-Sal', sign='Libra, the Scales', element='Aether')



    def test_getting_all_espers(self):
        """CHECKING IF ALL ESPERS ARE CORRECTLY BEING TAKEN"""

        all_espers = Esper.objects.all().count()

        self.assertEquals(all_espers, 13)

    def test_getting_espers_by_name_esper(self):
        """CHECKING IF THE NAME_ESPER IS CORRECTLY BEING TAKEN"""

        names = ['zodiark', 'belias', 'zalera']

        all_espers = [True if Esper.objects.get(pk=name.capitalize()) else False for name in names]
        true_list = [True, True, True]
        
        self.assertEquals(all_espers, true_list)
    
    def test_getting_espers_by_element(self):
        """CHECKING IF THE NAME_ESPER IS CORRECTLY BEING TAKEN"""

        elements = ['darkness', 'fire', 'death', 'gravity', 'lightning', 'soul', 'wind', 'holy', 'poison', 'earth', 'ice', 'water', 'aether' ]
        all_espers = [True if Esper.objects.get(element=elem.capitalize()) else False for elem in elements]
        true_list = [True, True, True, True, True, True, True, True, True, True, True, True, True]
        
        self.assertEquals(all_espers, true_list)

    def test_get_all_esper_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST ALL ESPERS USING SELENIUM | URL: espers/all"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/all')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')
    
    def test_get_all_esper_with_limit_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST LIMIT 1 PARAM ESPERS USING SELENIUM | URL: espers/all?limit=3"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/all?limit=3')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_all_esper_with_limit_str_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT STR 1 PARAM ESPERS USING SELENIUM | URL: espers/all?limit=error"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/all?limit=error')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')

    def test_get_all_esper_with_limit_zero_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 411 | TEST LIMIT=0 1 PARAM ESPERS USING SELENIUM | URL: espers/all?limit=0"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/all?limit=0')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '411')

    def test_get_all_esper_with_limit_param_error_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT WRONG WRITED 1 PARAM ESPERS USING SELENIUM | URL: espers/all?limited=3"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/all?limited=3')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')


    def test_get_filter_esper_by_name_esper_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST NAME_ESPER ESPERS  USING SELENIUM | URL: espers/filter?name_esper=zodiark"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?name_esper=zodiark')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_filter_esper_by_element_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST ELEMENT ESPERS  USING SELENIUM | URL: espers/filter?element=gravity"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?element=gravity')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_filter_esper_error_parameter_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST PARAM ERROR ESPERS  USING SELENIUM | URL: espers/filter?name_esper_error=zodiark"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?name_esper_error=zodiark')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')

    def test_get_filter_esper_error_parameter_value_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 404 | TEST WRONG VALUES ESPERS  USING SELENIUM | URL: espers/filter?name_esper=zodiarkkk"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?name_esper=zodiarkkk')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '404')


    def test_get_filter_esper_error_parameter_value_with_limit_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 200 | TEST LIMIT 2 PARAM ESPERS  USING SELENIUM | URL: espers/filter?name_esper=zodiarK?limit=1"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?name_esper=zodiark&limit=1')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '200')

    def test_get_filter_esper_error_parameter_value_with_limit_zero_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 411 | TEST LIMIT=0 2 PARAM  ESPERS  USING SELENIUM | URL: espers/filter?name_esper=zodiark&limit=0"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?name_esper=zodiark&limit=0')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '411')

    def test_get_filter_esper_error_parameter_value_with_limit_str_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT STR 2 PARAM  ESPERS USING SELENIUM | URL: espers/filter?name_esper=zodiark&limit=error"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?name_esper=zodiark&limit=error')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')

    def test_get_filter_esper_with_limit_param_error_web(self):
        """CHECKING IF THE RETURN IS EQUAL TO 400 | TEST LIMIT WRONG WRITED 2 PARAM ESPERS  USING SELENIUM | URL: espers/filter?name_esper=zodiark&limited=2"""
        browser.get('http://127.0.0.1:8000/ffxii/')
        form_input = browser.find_element(By.ID, 'url')
        form_submit = browser.find_element(By.ID, 'submit')
        form_input.send_keys('espers/filter?name_esper=zodiark&limited=2')
        form_submit.click()
        sleep(time_wait_answer)
        search_status = browser.find_element(By.ID, 'request-status')
        status = search_status.get_attribute('response')
        self.assertEquals(status, '400')