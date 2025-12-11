from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import datetime

def test():
          
          driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          def timer(driver,by,selector,timeout=10):
                  return WebDriverWait(driver,timeout).until(EC.element_to_be_clickable((by,selector)))
          def visible(driver,by,selector,timeout=10):
                  return WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((by,selector)))
          try:
                  timestamp= datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                  try:
                    print("abriu")
                    driver.get("http://127.0.0.1:5000/")
                  except Exception as e:
                       driver.save_screenshot(f"erros/erro_{timestamp}.png")
                       print(f"erro ,{e}")  
                  print("abrindo login")
                  try:
                    timer(driver,By.TAG_NAME,"a").click()
                  except Exception as e:
                       print(f"erro,{e}")
                       driver.save_screenshot(f"erros/erro_{timestamp}.png")
                  timer(driver,By.NAME,"email").send_keys("jose@gmail.com")
                  timer(driver,By.NAME,"senha").send_keys("123")
                  try:
                    timer(driver,By.ID,"btn").click()
                  except Exception as e:
                       print(f"erro,{e}")
                       driver.save_screenshot(f"erros/erro_{timestamp}.png")
                  print("cadastrou")
                
                  print("recebendo produto")
                  produto_id=25 # mude o numero 25 para o id de algum produto que voce tenha cadastrado no banco

                  recebimento=timer(driver,By.CSS_SELECTOR,f"button[data-produto-id='{produto_id}']")
                 
                  recebimento.click()
                  if recebimento:
                     visible(driver,By.CSS_SELECTOR,f"#form-{produto_id} input[name='local_entrega']").send_keys("tapera ,numero 435")
                     visible(driver,By.CSS_SELECTOR,f"#form-{produto_id} input[name='quantidade_receber']").send_keys(1)
                     timer(driver,By.CSS_SELECTOR,f"#form-{produto_id} #botao").click()
                     print("recebimento conlcuido")
                     
                  visible(driver, By.TAG_NAME, "h1")

                  timer(driver,By.ID,"movimentos").click()
                  print("movimentacoes abertas:")
                  movimentos=driver.find_elements(By.CSS_SELECTOR,"body li")
                  with open("relatorios/movimentacoes.txt", "w", encoding="utf-8") as f:
                           pass  

                  with open("relatorios/movimentacoes.txt","a",encoding="utf-8") as arquivo:
                    try:
                       for m in movimentos:
                          print(m.text)
                          arquivo.write(m.text +"\n")
                    except Exception as e:
                          print(f"nao funcionou, {e}")
                          driver.save_screenshot(f"erros/erro_{timestamp}.png")

                  print("\n")
                  timer(driver,By.TAG_NAME,"a").click()
                  print("produtos disponiveis: ")
                  produtos=driver.find_elements(By.CSS_SELECTOR,"body li")
                  with open("relatorios/produtos.txt","w",encoding="utf-8") as arquivo:
                    try:
                     for p in produtos:
                         print(p.text)
                         arquivo.write(p.text +"\n")
                    except Exception as e:
                          print(f"nao funcionou, {e}")
                          driver.save_screenshot(f"erros/erro_{timestamp}.png")
          except Exception as e:
                  print(f"nao funcionou, {e}")
                  driver.save_screenshot(f"erros/erro_{timestamp}.png")

          finally:
                  driver.quit()
if __name__=="__main__":
        test()