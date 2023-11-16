# Generated by Django 4.2.5 on 2023-11-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_rename_services_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfQAAAEsCAYAAAA1u0HIAAAAAXNSR0IArs4c6QAAHwVJREFUeF7t3WfT7DYZBmAHCKEESOgEQk2h/P9/ka90CJ0ktNASQj3Ms8QHHx3vWl7LtixfO8NkhuOV5evRu7cle71PvPLKKw86LwIECBAgQODQAk/UHuhPdF3njOPQY0znCRAgQGADgeoDfQOD5btw1rHcUAsECgj4UyyAqInDCgj0w5ZOxwkcRUDMHqVS+nlsAYF+7PrpPQECBAgQuAgI9BYHgglRi1V1TIUE/HkUgtRMdQICvbqS1N4hH4e1V0j/pgWM4mkjWxxPQKAfr2Z6TOAUAkL3FGXe7iBPMKBmBPoJNLYbWvZEgAABAgSKCswI9KL71RgBAgQIECBQUECgF8TUVKUCFpcqLYxuESBQUkCgl9TUFgECBAgQ2ElAoO8Eb7cECBAgQKCkgEAvqaktAgQOKOCazAGLVqDL7dVdoBcYFpogQIAAAQJ7Cwj0vStg/wQIECBAoICAQC+AqAkCBAjUIrD2QvLa7V9z3Gu/tdQ1px8CPUfJNgQIECBAoHIBgV55gXTveAJmEsermR4TaEFAoLdQxZqPQbrVXB19I0CgIQGB3lAxHQoBAgTaFTA7mKqtQJ8S8u8LBfwR/g+Qw8KBRLEEoDaaFhDoTZfXwREgQIDAWQQE+lkq7TgJECBAoJ3VspFFP4FugJ9HwKr3eWrtSAmcUECgn7DoDpkAAQIE2hMQ6O3V1BERIECAwAkF2gt0y6onHMYOmQABAgTaC3Q1JUCAAAECJxQQ6CcsukMmQIAAgfYEBHp7NXVEBAgQIHAigf5Ks0A/UdEdKgECBOYLuDFpvtk+7xDo+7jbKwECBAgQKCog0ItyaowAgRICp5wTnvKgS4wWbfQCAn3rseCPdmtx+yNA4F4Bn1f3yu3yPoG+C7ud7iPg02kfd3slsLHASf/UBfrG48zuCBBoX+CkedJ+YSs/QoFeeYF0jwABAgQI5AgI9Bwl2xAgQIAAgcoFBHrlBdI9AgQIECCQIyDQc5RsQ4AAAQIEKhcQ6JUXSPcIEDiLgFvpzlLptY7zaqAbWmuRa5cAAQIECJQXMEMvb6pFAgQIECCwuYBA35zcDgkQIFC5gCXaygs03j2Bfsiy6TQBAgQIEHhUQKAbEQQIECBAoAEBgV51Ea17VV0enSNAgMBGAjlpINA3KobdECBAgACBNQUE+pq62iZAgAABAhsJCPSNoO2GAAECBAisKSDQ19TVNgECBAgQ2EhAoG8EbTcECBAgQGBNAYG+pq62CRDYRiDnFuBtemIvBHYTEOi70dsxAQIECBAoJyDQy1lqiQABAgQIrChweylKoK9Ir+musxJqFBAgQGAbAYG+jbO9ECBAgACBVQUE+qq8GidAwDLNmcfA2dbo9j1egX7mvzXHTqCYwL4fZMUOQ0P5Akqeb1V4y2v0VwNdrQpXQHMECBAgQGBFATP0FXE1TYAAAQIEthJYJ9BN77eqn/0QIECAAIGLwDqBDvf/Ak5ujAYCBJoW8CFXS3kFei2V0A8CBAgQILBAQKAvwPNWAgQI5AmYxeY5HXCrikor0A84fnSZAAECBAikAgLdmCBAgAABAhkCFU3GR3sr0DOKaBMCBAgQIFC7gECvvUL6R+BoArVPY47mqb8EMgUEeiaUzQgQWENA+q+h+r822a5nW2fLAr3OuugVAQIECBCYJSDQZ3HZmAABAgQI1Ckg0Ousi14RIECAAIFZAgJ9FpeNCRAgQIBAnQKrB7rbMuosvF4RIECAQFsCqwd6W1yOhgABAgQI1Ckg0Ousi14RIECAAIFZAgJ9FpeNCRAgQIBAnQICvc666BUBAgQIEJglcLBAd4vdrOraeLGAEbeYUAMECGwkcLBA30jFbggQIHBFwEmeoVGrgECvtTL6RYDAigJieUVcTe8kINB3grdbAgQIECgo4BytE+gFx5OmCBAgQIDAXgICfS95+yVAYFrArGva6ORbNDdEFhyQQD/5H4PDJ0CAAIE2BAR6G3V0FAQIEFgusGB2uHznWlgqINCXCno/AQIECBCoQECgV1AEXSBAgAABAksFBPpSQe8nQIAAAQIVCAj0CoqgCwQIECBAYKmAQF8q6P0EGhJwT1RDxXQopxMQ6KcreQsHLHZaqKJjIECgrIBAL+uptbMIOKc4S6UdJ4HDCAj0w5RKR+sUkOx11kWvCBxMoMBHiUA/WM11lwABAgQIjAkIdOOCAAECBAg0ICDQGyiiQyBAgAABAgLdGCBAgAABAg0ICPRZRSxw18Ks/dmYAAECBAjkCQj0PCdbESBA4D4B84D73LxrtoBAn00Wb/AXehebNxEgQIDAagICfTVaDRMgQIAAge0EBPoj1mbe2w09eyJA4CwCPlm3qbRA38bZXggQIECAwKoCAn1VXo0TIECAAIFtBAT6Ns72QqARAYunjRRy5mE0UvdGDuNa8QT6zGFtcwKPCzT+KaHkBAgcQkCgH6JMOkmAAAECBK7Ozbuue9AJdCOEAAECBAg0ICDQGyiiQyBQo0CrFyJaPa4ax5A+zRMQ6PO8bL2zgA/TnQtQ2e6Nh8oKoju7Cgj0XfntnACBuwWk+d103timgEBvs66OqnUBYdZ6hR0fgdkCAn02mTcQIBACzimMAwJ1CdQd6D4x6hotekPgEQF/oAYEgZoE6g70mqT0hQABAgQIVCwg0Csujq4RIECAAIFcAYGeK2U7AgQIECBQsUBTge6KXsUjTdcIELgt4APMCFko0FSgL7TwdgIECBAgcFgBgX7Y0uk4AQIECBD4v4BANxoIECBAgEADAgK9gSI6BAIECBAgINCNAQIECBAg0ICAQF+jiO5WXUNVmwQIECBwQ0CgGx4nFHDGdcKiO2QCzQsI9OZL7AAJHEvA6dax6qW39QgI9HpqoScECBAgsINAKyeRAn2HwWOXBAgQIECgtIBALy2qPQJnFmhlqnPmGjr2wwrcF+j+aA9b8KN0/L3vfW/39a9/vfvABz4wu8vvvPNO9+1vf3vyfZ/4xCe6T37yk90HP/jBLvbXv/797393b731Vvfb3/62++Mf/zjZTrrBhz/84e7Tn/5095GPfKR73/ve1z3xRPzBdN1//vOf7u9//3v3hz/84dJ27KfF1zPPPNN96lOf6j70oQ9dXPvjj+P9xz/+0f3+97/v3njjjbsO/TOf+UwXdXvqqae697znPZc2Hjx4cLH8y1/+cnGN/859rTUW5vbD9gSWCNwX6Ev26L0EMgQ+9rGPdV/+8pcvgTj3NRXo73//+7svfvGL3Uc/+tGHYTO2jwiKP//5z93Pf/7zSxDlvJ577rlLmA9PEMbeF8H+y1/+8q4Thpx+7LFNnHw9//zzlxOZPsSv9SOO/9e//vXl5CbnFSdJ0Xb899YrTpqizbDNOWFacyzkHFfT25j4bV5egb45uR3mCEQofv7zn384C8t5T7/NrUCP0PnSl77UPf3009lN/vWvf+1+9rOfddHurVecJMRMr585Tu3gn//85yV4ckNtqr09/z1cv/rVr15WO3JfEbi/+tWvLrPqW684QQjb3NWaOBGLlZWo2a1QX3Ms5BrYjkBJAYFeUlNbxQTiAzyWbeMVH9ARqrmz5AjKCIqxV8z6P/7xjz+yDP6nP/3p4VJtrAzEMnz8t59lxv4jdH/6059ePb7oa5yADGfmb7/9dveb3/zmEi5PPvnkpd0I/OGqw9/+9rfu1VdfnTxZKAa7UkMvvvjiZcWjf8VMOVY3wu3NN9+8hPHY8UdNw/XaMnl4xonCsO0I6Wg3lu7j0kjUM/xj9j68vBH218ZB9HOtsbAS8SmaPdukvvTxCvRT/Jkc7yCHAREf4LHsvXQmG4HyhS984WHo3pohfvazn+3if31A/+tf/+p+8YtfjPYhnZ3eOgFIZ5ux7e9+97vL8R31FWEarv3KRLi+/vrrl/+lr7GZfNT1Jz/5yejhxyWMqEMf1HECEFZxEpa+0hWSWNaPdiP009daY2HzGpZOhM0PwA5LCgj0kpraKibwzW9+8+HybXyIxyx27IN5zg5feOGFy8y7n/VPBWkERHzw92ESIfKjH/3osV1G4Hzuc597GGgxM//BD35wdbk3ZpRxPbifqd8KnjnHt+m2gyAZukYfYuZ8azUjjj9s+5Ola/WNf3/ppZcuN9fFK2b9r7322uiJQn/suTXO3a5vN3csbFoDOyOQCAh0Q6I6gVhejeXQWKaOVyy3f//731/Uz5gZf+UrX3nYZizLx+zt1h3RsYQby71x41S8rgVPhE60358oxMw0bvi69RoGSk5QLTr4Fd+cGsVKRoT52Ay670b6DYZrKzBxeSJOfPrgj8sTMQ5uXRdPTxbGTq7WHAsrUmt6S4GDrnwI9C0HSaP7Kj32Y1YcH+T9Eu7UjC+HNZ1FR5DHLHrq9bWvfa2Lr2FdmyGmgZZzohBtpf2J6+w//vGPp7pT3b/H7DmOJW6GixOwOOn5zne+M9nPb33rWw9vcouAjssZUefha3gfRfz/saISN7pNvb7xjW88nNXHCUYs0cd1/P611liY6pd/J7C2gEBfW1j7swXiemzc5R5L3XGNOZZZ439LXjHjjxlf/4o7q3OuWw/7Eu9NTy7Sk4+YEX73u9+d7Gr6tby4g/573/te1letho3HbDOOrV9FiH+LFY24NHBrJhurFTGb7V+3rk1PHszMDeI6eqxQxHfJ4zUWuvH/D1c+5qxixKrKs88+e2k7xk+6YrLWWJjJYHMCxQUEenFSDS4VGH4g9x/2EVhjDxSJGXHcTR2Bf+su+HvDIf36XDqzT2/ayp1pp6GWO7Mfs01nnBFicYd3fCXu4WuwjJJuH2EZd4PHe7Z4pfuPk5lYnUi/FjicxV8L/bH+pidh6cx+rbGwhZ19ELglcKBAL72wa2DUKjBcMo2Qjpnm1Peb4wM/ZmLXnkCWs8Q75pFex02/4x7faY9Zev/KXRaO7e/t01g/hydB8e9xghDL0+m17HRGn/OVvJLjJKziJKi/P2L05KPrLvckzL3noe9nepKVnoTd6z41Fko6aYvAPQIHCvR7Ds97jiYQD3yJD/LhEnLuMcRMM5bE06X0JbPhNFjSpfGp5d1bfU9ninEdOU4I7nmNfR0sgixmvv3S+9h3urf4Hnz0LW50jCX+uOY+fIpcrK7ENxjSywNjlyRyHucbdmnwDgN9zbFwT92O9B5TqvqrNQh05aq/XO33ML1LuT/iCJ4Iu1jSjll7XCON/0VQDB/mEqEes/ThXeZLZntT773nDvf+mJa8d2wkpA+3CYvhw1XiwTfxLPQ+UGNVI2bx9zyvPmck3nraX/Qt9hsnX2PX+pfMhm+9d6qet45ryXtzvGxDYKmAGfpSQe8vKpAul6ahlO5s7LGg6fe6l3wQT713SSgvee819PTpZ/2T2OKkJy4P9N99n3ItUdS0lsM2o0YR6HHCMXbvg0AvUQFtnE1AoDdb8WOuuMQDWuI6a/8rZVMPf4nyxdfKhmEV12Vjlt4/9nMqlJfMypaE8pL3Xuvz2NJ7XEePa9b9A1rivbHU/cMf/nDV0Z/eXzC2swjzqFP6FECBvmppNN6ogEBvtLBlD6v+k4P0a1jDr4+dKdCj7umT6NKxELPj+Frb1I/NLB1DcUkkVgbi5KG/TBJ9i8skwx+wiaX/CPXh/QMCfam+959RQKAfqer15+pummkARIDEk+DiO9lnC/QoQvrVrb4wub9wtmYhI9Sjf/2d7rGv9IluAn3NCmi7VQGB3mplT3ZcaWgPHyeaPmp0zne+p+5yHz6kZOwhJrfKMP8u9/wzurE72qN/8S2AnKetrT180hvm4pp+fG++/ynV9PG/U79xP+zvrbvc1xwLa5tpn8CUQBuBnv85N+Xh3w8qkH4dKX2c6FrfPa7le+hjZUt/NCW2ufYDM3uU/eWXX37kd+mH3+Ffsqrie+h7VNM+axBoI9BrkNSHXQVuzdCjY+lsOPfJaHOfFBfPDI/vVU+9lnwfeqrt+PcItfiK2vBadfz/Y1/rG2tvi3Pk9GQotUufFDf1oy/9ccx9UlypsZBTF9sQWFNAoK+pq+3ZArEkOrxpKv3BjmsNpg8iSZfVh+Fx7elkY21PhUP6vfncX4Zb8uCUKdSx57sP37Plc9tv9TUN9PTO+xdffPEyFvoTkdzgnXrYz1pjYaou/p3A2gICfW1h7WcLpOEYoRyzsvign3qN/Sb58EdS7v11s6nnfuf+xGra/3ufAT/lMHbtvPfrwzHauPaEtqn203+PrxlG3eIGt1gNmHONPn1cbfrY3PTX1nJ+UCeOP5by+0cF5/zaWu7z96fGwlw727ctsMUqVyoo0NseU4c6ujQc5/zCVno9Nv3wT5fkr/22+RAs96dRxz7o33j99e7BDf3h9e25N9PdKmo8DS4uE/RL7f1sPN4TM9PhM9SH39W/d6BEoMf/+qfPjf3++Fjbcckhfpo2/tvPwOMHduJ5/P0rvbktp+30pHDsN9TXHAv3OnofgRICAr2EojaKCaQ3cuU8azy9XnztkaZpiE7NJiMAI1T6sLp2Q1k6+5/qczw4J5by+0fW5pxc5ADHMv4wtLd49Gu6z9yTk5h9h0NvO2YQPnGy1D8QJ+f6/3CZPsyuzerXGgs5dbJN13V7TF9PAC/QT1DkIx1iGnYRELEkGl+1Gnvmd8xGI9CHz3OPp47Fd9DTV9p2tBez1LHfWo9ZZ9xU1rcb28bXqsZ+PCV9Olv0OZa0ow9jPzry/PPPP/wt8Ohj+hvr99Qr+hkhFT9u07/SZfXYJmbFMUPtXzm/nT7Vn/QkLC6VhFX69Le+nXQVIbyuPREwvTQx9hCavt30BOzW1xPXGgtTVv6dwJoCAn1NXW3fJZA+jzwaiaebxYd+hETM5mJpNWbPEWDDO7mnZsfpddsIk5h5R9vx35hxxod9/Hf4q2DXThL6Axz7IZLoS8wQ472x1B3tRp/756nHe6f6mwuYzniv/Xzq2GNycx6ve6sfYzfhxWw6Tiji2OPu9fj1vNh3GKQ/hXvrev7YiUqcJMVJXti+9dZbl7EQP0wTl0j6mqWP/x3r/1pjIbdmtiNQWkCglxatpr3jrmmN3diVwxqhHz9Bmv4G+PC9Y886n2o7ZrGxQjD1qNSxE5FbbU/NZKf61f/72KrGrevj6Z37t1Yf5vQhZt7Dk5Wc90Ygx42Pt2zj5CpOWHJ/UndqVafv15pjIefYbUOgtIBALy2qvSICEeoRPDH7Sr9Lne4gPsDjN68jzKdCN94bH+Sx7B0zy+EsfKzdmD3GT3yO/SLY2IFGuzELH14CGNsuTj5iWXrpT5fm/A56uv/02nSplYLwjJoNfwTm2mCY+vnU9H25bUe7sSoQtmOXaNJ21xwLRf4QNEJghoBAn4Fl0+0FYhk1llPjAz1mf324R4jHB3bc+RxLr/cEYwRvvwQ8DOBot//99dzvwQ9los+xBN/3uT9piLCJE4Poa9zNnRM4U+LpqsC1pfZLO4NFm/QHXMIzgjBmy0tf/aWFCMtwHR5/XAOPk69+uXzuvuK+hqjbU089NToWYmUi52uO6X7XGgtzj6/Z7Y+7YHiokgj0Q5VLZwkQIECAwLiAQDcyCJxewPTp9EMAQBMCAr2JMjoIArUIODmopRL6cT4BgX6+mjtiAgQIEGhQQKA3WFSHRIAAAQLnExDo56u5IyZAgACBBgUEeoNFdUhLBO68Bnzn25b01HsJECAwFBDoRxwPwuOIVdNnAgQIrCog0Ffl1TgBAgQIENhGQKBv42wvBAgQIEBgVQGBvirveONWzHdAt0sCBA4q4BMzt3ACPVfKdgSKCviQKsqpMQIEOoFuEBAgQIAAgQYEBHoDRXQIBJoRsHDRTCkdyPYCAn17c3vcWkBIbC1ufwQI7CAg0HdAt0sCBAgQIFBaQKCXFtUeAQIECBDYQUCg74BulwQIECBAoLRAtYHusmfpUpdpT13KOGqFQD0C7/5V++OupyR39uSRQFfPOxW9jQABAgROL7B3hlY7Qz/9yABAgAABAgRmCAj0GVg2JUCAAIGNBPae7m50mCV3I9BLamqLAAECBAjsJCDQd4K3WwIECNQmYFJcW0Xm9Uegz/OyNQECBAgQqFJAoFdZFp0iQIAAAQLzBAT6PC9bH0rAAuKhyqWzBAgsEhDoi/i8mQABAgQI1CEg0Ouog14QIECAAIFFAgJ9EV/5N1skLm+qRQIECPxPoO1PWIFunO8n0Pbf1n6u9kyAwOYCNXycCfTNy26HBAgQIECgvEDTgV7DGVP5kmmRAAECBAg8LtB0oCs4AQIECBA4i0B+oJvunmVMOE4CBAgQOKBAfqAf8OB0mQABAusKmOms66v1OQICfY6WbQkQIECAQKUCAr3SwugWAQK3BMyMjQ8CqYBANyYIECBAgEADAgI9q4hmA1lMNiJAgACB3QSOG+gydrdBY8cECBAgUJ/AcQN9d0tnFLuXQAcIECCwi0Cdn/8CfZfBYKcECBAgQKCsgEAv66k1AgQIECCwi4BA34XdTgkQIECAQFkBgV7WU2sECBAgQGAXAYG+C/tWO63zxo2tjt5+CBAgcCaBooEuPrYfOsy3N7+5RwWprCC6Q+A8AkUD/TxsjpQAAQIE2hU45pm5QG93RDoyAgQIEDiRgEA/UbEdKgECBAi0KyDQ262tIyNAgMD2Asdcrd7eaYU9CvQVUGtq0t9WTdXQFwIECKwnINDXs9UyAQIECBC4CGwxuRLoBhsBAgQIvCuwRezAXktAoK8lq10CBAgQILChgEDfENuuCBAgQIDAWgICfS1Z7TYsYFmy4eI6NAKHFRDohy2djhMgQIAAgf8LCHSjgQABAgQINCAg0BsookMgQIDA5gJHv/J09P6PFFygb/5XYIcECBAgQKC8wLkCvcEzsvJDQosECBAgcESBcwX6ESukzwQIHFbAHOKwpTtkxwX6Icum0wSOKiDijlo5/a5fQKDXXyM9JECAAAECkwICfaOH5k9WImMDc5sMJJsQIEDgpAIC/aSF3/WwnZlsz898e3N7JLCxwEkC/d1PMx9qGw8vuyNAgACBrQROEuhbcR57P0c/3zl6/489evSewJ0C/nDvhHv8bQK9GOVRG/LXdNTK6TcBAgSGAgL9jONBhp+x6o6ZAIExgYY+DwW6IU6AQJMCVX5OV9mpJst/yoMS6Kcsu4MmUJuApKutIvpzPAGBfryard5jH62rE9sBAQIEigsI9OKkGiRAgAABAtsLCPTtze2RAAECBAgUFxDoxUk1SIAAAQIEthcQ6Nub2yMBApUIuF+kkkLoRhEBgV6EcaVGfNqsBKvZXQSM513Y7fQ8AgL9PLV2pCsLyKuVgfdqXmH3krffmQICfSaYzQ8q4EP5oIXTbQIEcgUEeq6U7Y4jILyPUys9JUCgmIBAL0apIQLnFXAOdd7aO/J6BAR6PbXQEwIECBAgcLeAQL+bzhsJECBAgEA9AgK9nlroCYGNBSyUbwxud5sJnHNsC/TNBthBdnTOv4ODFEc3CRAgcF1AoBsdBAgQIECgAYEKA90UsYFx5RAIECBAYGOBCgN9YwG7GxFwUmVYECBA4GgCAv1oFdPfruuccBgGjQgYyssLeXTDgv0X6MuHkxYIECBAgMDuAncGesFTit0JdIAAAQIECOQJ1Jx+dwZ63oHbigABAgQIENhGQKBv42wvBAgQIEBgVQGBviqvxgkQIECAwDYCAn0bZ3shQIAAAQKrCgj0VXk1ToAAAQIEthEQ6Ns4t7uXmm/5bFfdkREgQOAxAYFuUBAgUJmAs8TKCqI7BxEQ6AcplG4SIECAAIFbAk0GuvN7g54AAQIEahDYMo+aDPQaiqgPBAgQuC6w5GN+yXvVpGWBgoFukLU8UBwbAQIECNQtUDDQ6z5QvSNAgAABAi0LCPSWq+vYCBB4V8AKoqHQvoBAb7/GjpAAAQIETiAg0E9QZIdIgAABAu0LCPT2a+wICRAgQOAEAgL9BEXOOcThFUZXG3PEbEPgcQF/O0bFngICfU99+yZAgAABAoUEBHohSM0QIFCHgFlyHXXQi+0FBPr25vZIgAABAgSKCwj0YqTmBcUoNUSAAAECswUE+mwybyBAgAABAvUJCPT6aqJHBAgQIEBgtoBAn03mDQQIELhTwJW5O+G8LUdAoOco2YYAAQKnFHAGcqSyC/QjVUtfCRAgQIDAFQGBbmgQeETAjMSAIEDgmAIC/Zh102sCBAgQIPDodOSVV155wIQAAQIECBA4toAZ+rHrp/cECBAgQOAiINANBAIETiHg7ohTlPnUBynQT13+Cg/ep26FRdElApkC/n4zodbZTKCv46pVAgQIECCwqYBA35TbzggcS8CE61j10ttzCwj0c9ff0bcoIIVbrGpzx2SYli+pQC9vqkUCBAiMC0gxI2NFAYG+Iq6mCRAgQIDAVgICfStp+yFAgACBcgJWOx6zFOjlhpeWCBAgQIBAWYEZJy4CvSy91ggQIECAwC4CjwX6jJOBXTpspwcQMIgOUCRdJLCCgL/9FVDzmzRDz7ey5ckFfFadfAA4fAKVC+wW6D4cKx8ZukeAAAEChxLYLdAPpTSzs5ucrGyyk5kHbnMCBKoSqO1jorb+rFasawe6MoBAX62iGiZAgAABAtsJ/Bc8OdUSt0ls6wAAAABJRU5ErkJggg==', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
