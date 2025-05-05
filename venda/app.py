from flask import Flask, render_template, request, redirect
from models.cliente import Cliente
from models.produto import Produto
from models.venda import Venda
from models.item_venda import ItemVenda

from controllers.cliente_controller import ControleCliente
from controllers.produto_controller import ControleProduto
from controllers.venda_controller import ControleVenda
from controllers.item_venda_controller import ControleItemVenda

from datetime import datetime

app = Flask(__name__)

# ROTA PRINCIPAL
@app.route("/")
def home():
    return render_template("home.html")

# ====================
# CLIENTE
# ====================
@app.route("/clientes")
def listar_clientes():
    dao = ControleCliente()
    dados = dao.listarTodos(Cliente())
    lista = [dao.converteObjeto(x) for x in dados]
    return render_template("lista_clientes.html", lista=lista, titulo="Clientes")

@app.route("/cliente/novo", methods=["GET", "POST"])
def novo_cliente():
    if request.method == "POST":
        cliente = Cliente()
        cliente.nome = request.form["nome"]
        cliente.endereco = request.form["endereco"]
        dao = ControleCliente()
        dao.incluir(cliente)
        return redirect("/clientes")
    return render_template("cadastro_cliente.html", titulo="Cadastrar Cliente")

# ====================
# PRODUTO
# ====================
@app.route("/produtos")
def listar_produtos():
    dao = ControleProduto()
    dados = dao.listarTodos(Produto())
    lista = [dao.converteObjeto(x) for x in dados]
    return render_template("lista_produtos.html", lista=lista, titulo="Produtos")

@app.route("/produto/novo", methods=["GET", "POST"])
def novo_produto():
    if request.method == "POST":
        produto = Produto()
        produto.nome = request.form["nome"]
        produto.preco = float(request.form["preco"])
        dao = ControleProduto()
        dao.incluir(produto)
        return redirect("/prod utos")
    return render_template("cadastro_produto.html", titulo="Cadastrar Produto")

# ====================
# VENDA
# ====================
@app.route("/vendas")
def listar_vendas():
    dao = ControleVenda()
    dados = dao.listarTodos(Venda())
    lista = [dao.converteObjeto(x) for x in dados]
    return render_template("lista_vendas.html", lista=lista, titulo="Vendas")

@app.route("/venda/nova", methods=["GET", "POST"])
def nova_venda():
    if request.method == "POST":
        venda = Venda()
        venda.data = datetime.now().strftime("%Y-%m-%d")
        venda.valor_total = float(request.form["valor_total"])
        venda.codcliente = int(request.form["codcliente"])

        ctrl_venda = ControleVenda()
        ctrl_item = ControleItemVenda()
        ctrl_produto = ControleProduto()

        # Grava venda
        ctrl_venda.incluir(venda)

        # Recupera último ID de venda (assumindo auto incremento com maior valor)
        todas = ctrl_venda.listarTodasVendas()
        id_venda = max(x[0] for x in todas)

        # Grava itens da venda
        produtos = request.form.getlist("produtos[]")
        quantidades = request.form.getlist("qtde[]")

        for i in range(len(produtos)):
            qtde = int(quantidades[i])
            if qtde > 0:
                item = ItemVenda()
                item.codvenda = id_venda
                item.codproduto = int(produtos[i])
                produto = Produto()
                produto.codproduto = item.codproduto
                produto = ctrl_produto.pesquisaCodigo(produto)
                item.valor = float(produto.preco)
                item.qtde = qtde
                ctrl_item.incluirItem(item)

        return redirect("/vendas")

    dao_cliente = ControleCliente()
    dao_produto = ControleProduto()
    clientes = [dao_cliente.converteObjeto(x) for x in dao_cliente.listarTodos(Cliente())]
    produtos = [dao_produto.converteObjeto(x) for x in dao_produto.listarTodos(Produto())]

    return render_template("nova_venda.html", clientes=clientes, produtos=produtos, titulo="Nova Venda")


    dao = ControleCliente()
    dados = dao.listarTodos(Cliente())
    clientes = [dao.converteObjeto(x) for x in dados]
    return render_template("nova_venda.html", clientes=clientes, titulo="Nova Venda")

@app.route("/cliente/editar/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    dao = ControleCliente()
    cliente = Cliente()
    cliente.codcliente = id
    cliente = dao.pesquisaCodigo(cliente)

    if request.method == "POST":
        cliente.nome = request.form["nome"]
        cliente.endereco = request.form["endereco"]
        dao.alterar(cliente)
        return redirect("/clientes")

    return render_template("editar_cliente.html", cliente=cliente, titulo="Editar Cliente")

@app.route("/cliente/remover/<int:id>")
def remover_cliente(id):
    dao = ControleCliente()
    cliente = Cliente()
    cliente.codcliente = id
    dao.deletarCliente(cliente)
    return redirect("/clientes")

@app.route("/produto/editar/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    dao = ControleProduto()
    produto = Produto()
    produto.codproduto = id
    produto = dao.pesquisaCodigo(produto)

    if request.method == "POST":
        produto.nome = request.form["nome"]
        produto.preco = float(request.form["preco"])
        dao.alterar(produto)
        return redirect("/produtos")

    return render_template("editar_produto.html", produto=produto, titulo="Editar Produto")

@app.route("/produto/remover/<int:id>")
def remover_produto(id):
    dao = ControleProduto()
    produto = Produto()
    produto.codproduto = id
    dao.deletarProduto(produto)
    return redirect("/produtos")

@app.route("/venda/<int:id>")
def detalhes_venda(id):
    ctrl_venda = ControleVenda()
    ctrl_cliente = ControleCliente()
    ctrl_item = ControleItemVenda()
    ctrl_prod = ControleProduto()

    # Venda
    venda = Venda()
    venda.codvenda = id
    venda = ctrl_venda.pesquisaCodigo(venda)

    # Cliente
    cliente = Cliente()
    cliente.codcliente = venda.codcliente
    cliente = ctrl_cliente.pesquisaCodigo(cliente)

    # Itens
    itens_raw = ctrl_item.listarItensPorVenda(id)
    itens = []
    for item in itens_raw:
        produto = Produto()
        produto.codproduto = item[1]
        produto = ctrl_prod.pesquisaCodigo(produto)
        itens.append({
            'nome': produto.nome,
            'qtde': item[2],
            'preco': item[3],
            'subtotal': item[2] * item[3]
        })

    return render_template("detalhes_venda.html", venda=venda, cliente=cliente, itens=itens)



if __name__ == "__main__":
    app.run(debug=True)
